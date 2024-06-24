from tqdm import tqdm


class loader():
    def load_file(self, file_name):
        self.file_name = file_name
        input_urls = []
        with open(file_name, 'r') as file:
            for line in tqdm(file):
                url = line.strip()
                input_urls.append(url)
        print('index_urls load complete')
        return input_urls
