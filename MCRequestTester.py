import os
class MCRequest():

    def __init__(self,prepid,alias,NEVENT=5000):
        ##--
        self.prepid = prepid
        self.alias  = alias
        self.setup=''##setup script contents
        self.exe='' ## executable contents
        self.jds='' ## jds contents
        self.PythonFileName=''
        self.nThreads=''
        self.workdir=self.alias+'_workdir'
        #self.setupscript=self.alias+'_setup.sh'
        self.GetSetupScript()
        self.SetNEvent(NEVENT)
        self.SetExe()
        self.SetJds()
    def GetSetupScript(self):
        command='wget --no-check-certificate https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/'+self.prepid
        os.system(command)
        f=open(self.prepid,'r')
        self.setup=f.readlines()
        f.close()
        #os.system('mv '+self.prepid+' '+self.prepid+'_source.sh')
        os.system('rm '+self.prepid)
        self.GetNCPU()


    def GetOptionArgument(self,line,option):
        argument=''
        
        if option+' ' in line:
            argument=line.split(option+' ')[1].split()[0]
        return argument
                
    def SetNEvent(self,NEVENT):

        lines=self.setup
        newlines=[]
        for line in lines:
            if '-n ' in line and 'cmsDriver.py' in line:
                oldNEVENT=self.GetOptionArgument(line,'-n')
                line=line.replace('-n '+oldNEVENT,'-n '+str(NEVENT))
            newlines.append(line)
        self.setup=newlines
        

    def GetPythonFileName(self):
        #--python_filename
        lines=self.setup
        ans=''
        for line in lines:
            if '--python_filename' in line and 'cmsDriver.py' in line:
                ans=self.GetOptionArgument(line,'--python_filename')
                #line.split('--python_filename ')[1].split()[0]
        return ans
    #def ProduceSetupScript():
    #    f=open(self.setupscript,'w')
    #    for line in self.setup:
    #        f.write(line)
    #    f.close()
    

    def SetExe(self):
        self.PythonFileName=self.GetPythonFileName()
        self.exe='cmsRun '+self.PythonFileName
        self.exe=self.exe.split('\n')
    def GetNCPU(self):
        #--nThreads
        lines=self.setup
        ans=''
        for line in lines:
            #print line
            if '--nThreads' in line and 'cmsDriver.py' in line:
                ans=self.GetOptionArgument(line,'--nThreads')
                #print 'ans=',ans
        self.nThreads=ans
        if ans=='':self.nThreads=1

    def ExportExe(self):
        f=open(self.alias+'_exe.sh','w')
        
        for line in self.setup+self.exe:
            #if 'slc6' in line:line=line.replace('slc6','slc7')
            f.write(line)
            if '#!/bin/bash' in line: 
                f.write('cd ${_CONDOR_SCRATCH_DIR}\n')
        f.close()
        os.system('chmod 777 '+self.alias+'_exe.sh')
    def SetJds(self):
        self.jds="""
executable = {0}
universe = vanilla
output = {1}
error = {2}
log = {3}
request_cpus = {4}
accounting_group=group_cms
JobBatchName = {5}
requirements = ( HasSingularity == true )
+SingularityImage = "/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el6:latest"
+SingularityBind = "/cvmfs, /cms, /share"

queue
""".format(self.alias+'_exe.sh', self.alias+'.out', self.alias+'.err', self.alias+'.log', self.nThreads, 'RequestTest_'+self.alias)
        self.jds = self.jds.split('\n')
    def ExportJds(self):
        f=open(self.alias+'.jds','w')
        for line in self.jds:
            f.write(line+"\n")
        f.close()

    def CondorSubmit(self):
        maindir=os.getcwd()
        os.system('mkdir -p '+self.workdir)
        os.chdir(self.workdir)
        command='condor_submit '+self.alias+'.jds > '+self.alias+'.jid'
        print command
        os.system(command)
        os.chdir(maindir)
        
    def Run(self):
        #self.GetSetupScript()
        #self.SetNEvent(NEVENT)
        #self.SetExe()
        #self.SetJds()
        maindir=os.getcwd()
        os.system('mkdir -p '+self.workdir)
        os.chdir(self.workdir)
        #self.ExportSetup()
        self.ExportExe()
        self.ExportJds()
        os.chdir(maindir)
if __name__ == '__main__':
    mydict={
        'ggfhlnuqq_M200_5000events':{
            'prepid':'HIG-RunIIFall17wmLHEGS-01250',
            'NEVENT':5000
        }
    }

    for req in mydict: 
        mytest=MCRequest(mydict[req]['prepid'],req)
        mytest.Run()
        mytest.CondorSubmit()
        
