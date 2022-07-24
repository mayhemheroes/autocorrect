#!/usr/local/bin/python3
import atheris
import sys
import io
import os

import autocorrect
from autocorrect import Speller

autocorrect.PATH = "/autocorrect/autocorrect"

spell = Speller()
spell_fast = Speller(fast=True)

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    # try:
    #     txt = data.decode('utf-8')
    # except:
    #     return
    
    if len(data) > 1:  
        if fdp.ConsumeBool():
            spell(fdp.ConsumeString(len(data) - 1))
        else:
            spell_fast(fdp.ConsumeString(len(data) - 1))

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()