import re

class cleaner():
    def clean_url(self, raw, processed):
        with open(raw, 'r', encoding='utf-8') as file:
            raw_urls = file.readlines()
            file.close()
        cleaned_urls = set()
        for url in raw_urls:
            match = re.match(r'(https?://[^/]+)', url)
            if match:
                cleaned_urls.add(match.group(1))
                
        cleaned_urls = [url.strip() + '\n' for url in cleaned_urls if url.strip()]

        with open(processed, 'w', encoding='utf-8') as file:
            file.writelines(cleaned_urls)
            file.close()