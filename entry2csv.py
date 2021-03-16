#!/usr/bin/python

from ROOT import gROOT,gStyle,gPad,TFrame,TLine,TCutG,TFile,TCanvas,TH1F,TH2F,TGraph
from ROOT import TLegend
import ROOT as rt
import numpy as np
from tqdm import tqdm
from ctypes import *
from array import array
import sys
import pandas as pd


fcut = TFile('mycut.root')
cutg = fcut.Get('mycut')

rootFileInput = TFile('proc_alpha3.root')
tree = rootFileInput.Get('trigger_proc')

f = rt.TFile('alpha3.root')
t = f.Get('trigger')

#energy = array('d',[0]*2)
#raise_t = array('d',[0]*2)

#tree.GetBranch('trig_proc').SetAddress(evt_trig_stru)
#tree.GetBranch('raise_t[1]').SetAddress(raise_t)

c1 = TCanvas()
c1.Divide(2,1)
c1.cd(1)

#gPad.SetLogy()

h1 = TH2F('h1','',500,0,50000,500,0,50)


entries = tree.GetEntries()
with open('out1.txt','w') as fout:
    for i in tqdm(range(entries)):
        tree.GetEntry(i)
        h1.Fill(tree.energy[0],tree.raise_t[0])
        if cutg.IsInside(tree.energy[0],tree.raise_t[0]):
            fout.write(str(i))
            fout.write('\n')


h1.Draw('colz')

#####################################################

df = pd.read_csv("out1.txt", names=["value"], dtype=int)

data = []

for x in df["value"]:
    data.append(x)

#####################################################

c1.cd(2)

#t.GetBranch('trig_v1740').SetAddress(evt_trig_stru)

h2 = rt.TH2F('h2','',500,0,3200,500,700,1000)

k=0
i=0
j=0

entries = t.GetEntries()
with open('alpha1.csv','w') as fout:
    for i in tqdm(range(entries)):
        try:
            if i == data[k]:
                k+=1
                t.GetEntry(i)
        #h1.Fill(evt_trig_stru.sample00[3]:e)
                sum = [0.]*3072
                for j in range(3072):
                    sum[j] += t.sample00[j]
                    h2.Fill(j,sum[j])
                    fout.write(str(sum[j]))
                    if j == 3071:
                        continue
                    else:
                        fout.write(',')
                fout.write('\n')
        except:
            continue


h2.Draw('l')
input()
