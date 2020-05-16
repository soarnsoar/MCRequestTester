import os
from MCRequestTester import MCRequest

#HIG-RunIISummer15wmLHEGS-01741
#GluGluHToWWToLNuQQ_M300_13TeV_powheg_JHUgenv698_pythia8
if __name__ == '__main__':
    dirname='signal2016'
    nevent=10000
    samples={}
    samples["GluGluHToWWToLNuQQ_M115__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02427","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M120__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02544","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M124__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02545","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M125__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02407","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M126__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02546","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M130__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02547","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M135__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02548","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M140__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02549","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M145__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02550","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M150__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02551","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M1500__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02458","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M155__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02552","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M160__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02553","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M165__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02554","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M170__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02555","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M175__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02556","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M180__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02557","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M190__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02558","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M200__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02559","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M2000__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02459","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M210__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02560","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M230__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02561","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M250__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02562","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M2500__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02460","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M270__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02563","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M300__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02450","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M3000__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02461","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M350__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02449","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M400__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02451","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M4000__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02326","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M450__2016__"+str(nevent)]={"prepid":"HIG-RunIIWinter15wmLHE-00481","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M500__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02452","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M5000__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02327","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M550__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02453","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M600__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02454","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M700__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02455","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M750__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02564","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M800__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02456","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M900__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02457","NEVENT":nevent}

    samples["VBFHToWWToLNuQQ_M1000__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02479","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M115__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02565","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M120__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02566","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M124__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02567","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M125__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02408","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M126__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02568","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M130__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02569","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M135__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02570","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M140__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02571","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M145__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02572","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M150__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02573","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M1500__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02473","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M155__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02574","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M160__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02575","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M165__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02576","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M170__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02577","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M175__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02578","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M180__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02579","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M190__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02580","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M200__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02463","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M2000__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02474","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M210__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02581","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M230__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02582","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M250__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02464","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M2500__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02475","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M270__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02583","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M300__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02465","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M350__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02466","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M400__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02467","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M4000__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02330","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M450__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02482","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M500__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02584","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M5000__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02331","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M550__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02468","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M600__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02469","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M650__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02483","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M700__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02470","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M750__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02593","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M800__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02471","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M900__2016__"+str(nevent)]={"prepid":"HIG-RunIISummer15wmLHEGS-02472","NEVENT":nevent}
    




    os.system('mkdir -p '+dirname)
    os.chdir(dirname)
    for req in samples:
        mytest=MCRequest(samples[req]['prepid'],req,samples[req]['NEVENT'])
        mytest.Run()
        mytest.CondorSubmit()


