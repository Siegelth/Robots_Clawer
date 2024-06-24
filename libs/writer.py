import pandas as pd
import re
import pandas as pd
import re
import os


class Writer():
    def parse_robots_to_csv(self,website_url, robots_text):
        blocks = robots_text.strip().split("User-agent: ")
        data = []
        directive_pattern = re.compile(r"(Allow|Disallow):\s*(.*)")
        sitemap_pattern = re.compile(r"Sitemap:\s*(.*)")
        for block in blocks[1:]:
            lines = block.split("\n")
            user_agent = lines[0].strip()
            directives = directive_pattern.findall(block)
            sitemaps = sitemap_pattern.findall(robots_text)
            for directive, path in directives:
                data.append([website_url, user_agent, directive, path, ""])
            for sitemap in sitemaps:
                data.append([website_url, "", "Sitemap", "", sitemap])
        df = pd.DataFrame(
            data, columns=["URL", "User-agent", "Directive", "Path", "Sitemap"])
        file_exists = os.path.exists("robots_directives.csv")
        df.to_csv("robots_directives.csv", mode='a',
                  index=False, header=not file_exists)
