class get_dataset():
    from kaggle.api.kaggle_api_extended import KaggleApi
    import zipfile

    api = KaggleApi()
    api.authenticate()

    f = 'country_vaccinations.csv'
    dir='./'

    # Signature: dataset_download_file(dataset, file_name, path=None, force=False, quiet=True)
    api.dataset_download_file('gpreda/covid-world-vaccination-progress', f)

    api.dataset_download_file('imdevskp/corona-virus-report', 'country_wise_latest.csv')

    with zipfile.ZipFile(f+'.zip', 'r') as zip_ref:
        zip_ref.extractall(dir)