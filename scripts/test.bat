@echo off

if not exists testvenv call scripts\setuptest.bat

testvenv\Scripts\python test\tests.py
