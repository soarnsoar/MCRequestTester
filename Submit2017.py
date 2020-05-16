import os
from MCRequestTester import MCRequest

#HIG-RunIISummer15wmLHEGS-01741
#GluGluHToWWToLNuQQ_M300_13TeV_powheg_JHUgenv698_pythia8
if __name__ == '__main__':
    dirname='signal2017'
    nevent=10000
    samples={}
    samples["GluGluHToWWToLNuQQ_M1000__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03938","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M115__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03918","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M120__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03919","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M124__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03920","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M125__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01211","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M126__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03921","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M130__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03922","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M135__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03923","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M140__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03924","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M145__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03925","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M150__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03926","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M1500__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01262","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M155__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03927","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M160__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03928","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M165__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03929","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M170__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03930","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M175__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03931","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M180__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03932","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M190__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03933","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M200__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01250","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M2000__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01263","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M210__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03934","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M230__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03935","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M250__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01251","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M2500__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01264","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M270__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03936","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M300__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01252","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M3000__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01265","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M350__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01253","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M400__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01254","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M4000__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03815","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M450__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03968","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M500__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01255","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M5000__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03816","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M550__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01256","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M600__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01257","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M650__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01258","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M700__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01259","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M750__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03937","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M800__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01260","NEVENT":nevent}
    samples["GluGluHToWWToLNuQQ_M900__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01261","NEVENT":nevent}
    
    samples["VBFHToWWToLNuQQ_M1000__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01281","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M115__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03939","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M120__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03940","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M124__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03941","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M125__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01266","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M126__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03942","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M130__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03943","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M135__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03944","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M140__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03945","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M145__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03946","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M150__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03947","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M1500__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01282","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M155__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03948","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M160__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03949","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M165__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03950","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M170__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03951","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M175__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03952","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M180__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03953","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M190__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03954","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M200__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01267","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M2000__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01284","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M210__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03955","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M230__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03956","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M250__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01268","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M2500__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01285","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M270__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03957","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M300__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01269","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M3000__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01286","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M350__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01270","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M400__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01271","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M4000__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03817","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M450__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01272","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M500__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01273","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M5000__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-03818","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M550__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01274","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M600__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01275","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M650__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01276","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M700__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01277","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M750__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01278","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M800__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01279","NEVENT":nevent}
    samples["VBFHToWWToLNuQQ_M900__2017__"+str(nevent)]={"prepid":"HIG-RunIIFall17wmLHEGS-01280","NEVENT":nevent}



    
    os.system('mkdir -p '+dirname)
    os.chdir(dirname)
    for req in samples:
        mytest=MCRequest(samples[req]['prepid'],req,samples[req]['NEVENT'])
        mytest.Run()
        mytest.CondorSubmit()



