import os
from MCRequestTester import MCRequest

#HIG-RunIISummer15wmLHEGS-01741
#GluGluHToWWToLNuQQ_M300_13TeV_powheg_JHUgenv698_pythia8
if __name__ == '__main__':
    dirname='test2017qcd'
    samples={}
    samples["QCD_Pt-120to170_EMEnriched__2017__10000"]={"prepid":"EGM-RunIIFall17GS-00006","NEVENT":10000}
    samples["QCD_Pt-15to20_EMEnriched__2017__10000"]={"prepid":"EGM-RunIIFall17GS-00001","NEVENT":10000}
    samples["QCD_Pt-170to300_EMEnriched__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00030","NEVENT":10000}
    samples["QCD_Pt-20to30_EMEnriched__2017__10000"]={"prepid":"EGM-RunIIFall17GS-00003","NEVENT":10000}
    samples["QCD_Pt-300toInf_EMEnriched__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00031","NEVENT":10000}
    samples["QCD_Pt-30to50_EMEnriched__2017__10000"]={"prepid":"EGM-RunIIFall17GS-00002","NEVENT":10000}
    samples["QCD_Pt-30toInf_DoubleEMEnriched__2017__10000"]={"prepid":"HIG-RunIIFall17GS-00005","NEVENT":10000}
    samples["QCD_Pt-50to80_EMEnriched__2017__10000"]={"prepid":"EGM-RunIIFall17GS-00004","NEVENT":10000}
    samples["QCD_Pt-80to120_EMEnriched__2017__10000"]={"prepid":"EGM-RunIIFall17GS-00005","NEVENT":10000}
    samples["QCD_Pt-1000toInf_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00013","NEVENT":10000}
    samples["QCD_Pt-120to170_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00007","NEVENT":10000}
    samples["QCD_Pt-15to20_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00014","NEVENT":10000}
    samples["QCD_Pt-170to300_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00008","NEVENT":10000}
    samples["QCD_Pt-20to30_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00003","NEVENT":10000}
    samples["QCD_Pt-300to470_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00009","NEVENT":10000}
    samples["QCD_Pt-30to50_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00004","NEVENT":10000}
    samples["QCD_Pt-470to600_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00010","NEVENT":10000}
    samples["QCD_Pt-50to80_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00005","NEVENT":10000}
    samples["QCD_Pt-600to800_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00011","NEVENT":10000}
    samples["QCD_Pt-800to1000_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00012","NEVENT":10000}
    samples["QCD_Pt-80to120_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00006","NEVENT":10000}
    samples["QCD_Pt_170to250_bcToE__2017__10000"]={"prepid":"HIG-RunIIFall17GS-00080","NEVENT":10000}
    samples["QCD_Pt_20to30_bcToE__2017__10000"]={"prepid":"HIG-RunIIFall17GS-00077","NEVENT":10000}
    samples["QCD_Pt_20to30_bcToE_newpmx__2017__10000"]={"prepid":"HIG-RunIIFall17GS-00093","NEVENT":10000}
    samples["QCD_Pt_250toInf_bcToE__2017__10000"]={"prepid":"HIG-RunIIFall17GS-00081","NEVENT":10000}
    samples["QCD_Pt_30to80_bcToE__2017__10000"]={"prepid":"HIG-RunIIFall17GS-00078","NEVENT":10000}
    samples["QCD_Pt_80to170_bcToE__2017__10000"]={"prepid":"HIG-RunIIFall17GS-00079","NEVENT":10000}
    samples={}
    samples["QCD_Pt-120to170_MuEnrichedPt5__2017__10000"]={"prepid":"BTV-RunIIFall17GS-00007","NEVENT":10000}


    os.system('mkdir -p '+dirname)
    os.chdir(dirname)
    for req in samples:
        mytest=MCRequest(samples[req]['prepid'],req,reqsamples[req]['NEVENT'])
        mytest.Run()
        mytest.CondorSubmit()
