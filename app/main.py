#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(argv):
  for i, v in enumerate(argv):
    if v!="":
      print("Hello "str(v)+"!")
    else:
      print("Hello!")
