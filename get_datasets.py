class get_dataset():
    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()

    # Signature: dataset_download_file(dataset, file_name, path=None, force=False, quiet=True)
    api.dataset_download_file('gpreda/covid-world-vaccination-progress', 'country_vaccinations.csv')
