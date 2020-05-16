import os
from MCRequestTester import MCRequest

#HIG-RunIISummer15wmLHEGS-01741
#GluGluHToWWToLNuQQ_M300_13TeV_powheg_JHUgenv698_pythia8
if __name__ == '__main__':
    dirname='qcd2016'
    nevent=100000
    samples={}
    samples["QCD_Pt-120to170_EMEnriched__2016__"+str(nevent)]={"prepid":"TSG-RunIISummer15GS-00006","NEVENT":nevent}
    samples["QCD_Pt-120to170_EMEnriched_ext1__2016__"+str(nevent)]={"prepid":"TSG-RunIISummer15GS-00048","NEVENT":nevent}
    samples["QCD_Pt-170to300_EMEnriched__2016__"+str(nevent)]={"prepid":"TSG-RunIISummer15GS-00028","NEVENT":nevent}
    samples["QCD_Pt-20to30_EMEnriched__2016__"+str(nevent)]={"prepid":"SUS-RunIISummer15GS-00057","NEVENT":nevent}
    samples["QCD_Pt-300toInf_EMEnriched__2016__"+str(nevent)]={"prepid":"TSG-RunIISummer15GS-00029","NEVENT":nevent}
    samples["QCD_Pt-30to50_EMEnriched__2016__"+str(nevent)]={"prepid":"TSG-RunIISummer15GS-00003","NEVENT":nevent}
    samples["QCD_Pt-30to50_EMEnriched_ext1__2016__"+str(nevent)]={"prepid":"TSG-RunIISummer15GS-00037","NEVENT":nevent}
    samples["QCD_Pt-30toInf_DoubleEMEnriched__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15GS-00393","NEVENT":nevent}
    samples["QCD_Pt-50to80_EMEnriched__2016__"+str(nevent)]={"prepid":"TSG-RunIISummer15GS-00004","NEVENT":nevent}
    samples["QCD_Pt-50to80_EMEnriched_ext1__2016__"+str(nevent)]={"prepid":"TSG-RunIISummer15GS-00046","NEVENT":nevent}
    samples["QCD_Pt-80to120_EMEnriched__2016__"+str(nevent)]={"prepid":"TSG-RunIISummer15GS-00005","NEVENT":nevent}
    samples["QCD_Pt-15to20_MuEnrichedPt5__2016__"+str(nevent)]={"prepid":"BTV-RunIISummer15GS-00002","NEVENT":nevent}
    samples["QCD_Pt-20toInf_MuEnrichedPt15__2016__"+str(nevent)]={"prepid":"BTV-RunIISummer15GS-00001","NEVENT":nevent}
    samples["QCD_Pt_15to20_bcToE__2016__"+str(nevent)]={"prepid":"BTV-RunIISummer15GS-00014","NEVENT":nevent}
    samples["QCD_Pt_170to250_bcToE__2016__"+str(nevent)]={"prepid":"BTV-RunIISummer15GS-00018","NEVENT":nevent}
    samples["QCD_Pt_20to30_bcToE__2016__"+str(nevent)]={"prepid":"BTV-RunIISummer15GS-00015","NEVENT":nevent}
    samples["QCD_Pt_250toInf_bcToE__2016__"+str(nevent)]={"prepid":"BTV-RunIISummer15GS-00019","NEVENT":nevent}
    samples["QCD_Pt_30to80_bcToE__2016__"+str(nevent)]={"prepid":"BTV-RunIISummer15GS-00016","NEVENT":nevent}
    samples["QCD_Pt_80to170_bcToE__2016__"+str(nevent)]={"prepid":"BTV-RunIISummer15GS-00075","NEVENT":nevent}





    os.system('mkdir -p '+dirname)
    os.chdir(dirname)
    for req in samples:
        mytest=MCRequest(samples[req]['prepid'],req,samples[req]['NEVENT'])
        mytest.Run()
        mytest.CondorSubmit()



