FROM gcr.io/oss-fuzz-base/base-builder-python

RUN pip3 install atheris

COPY . /autocorrect
WORKDIR /autocorrect
RUN python3 -m pip install . && chmod +x fuzz/fuzz_spellcheck.py && wget http://ipfs.io/ipfs/QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/en.tar.gz && mv en.tar.gz autocorrect/data/en.tar.gz
