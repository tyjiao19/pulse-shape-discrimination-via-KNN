#include "TFile.h"
#include "TCutG.h"

   void SaveCuts(void){
   TFile *fcut=new TFile("mycut.root","recreate");
   fcut->cd();
   gROOT->FindObject("mycut")->Write();
   fcut->Close();
   }
   
   void LoadCuts(void){
   TFile *fcut=new TFile("cut0.root");
   TCutG *proton1=(TCutG *)fcut->Get("telp");
   fcut->Close();
   }
