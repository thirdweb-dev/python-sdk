# DO NOT RUN LOCALLY
pip install pydoctor && pydoctor --make-html --html-output=. nftlabs/modules && rm main.py && rm requirements.txt && rm setup.py && rm README.md  && rm -rf nftlabs && rm -- "$0"
