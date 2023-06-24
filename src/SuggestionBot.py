import src.Network as net;
import src.drive_access as drive;
import ast;
from collections import Counter
import random as random

class Sbot():
    db = 1;
    topicsheet = 1;
    def __init__(self,username,password):
        self.auth = drive.auth('client_secret.json');
        #print ("Authenticated!");
        username,password.strip();
        self.Login(username,password);
        if (self.LOGIN_STATUS==0): return;
        if (Sbot.db ==1):
            Sbot.db = drive.sheet(self.auth,"UserDB");
        self.SetupNetwork();
    
        
    def StartSession(self,Chapters,QuestionCount):#numeric values of chapters
        if(self.LOGIN_STATUS==0): print("Not logged in! Please restart the session with the correct credentials!"); return;
        self.setTopics(Chapters);
        self.blacklist = self.setupBlackList();
        self.desiredOutput = self.network.Calculate([1,1]);
        
        self.setupQuestions(self.topics,QuestionCount);
    
    #********************************************
    #TODO: Make the returned questions into a final list of the form: (Chapter,Question)
    #ProcessQuestions is done, just add return statement and remove the print statement
    #follow algorythm written in my notebook!
    
    def setupQuestions(self,Topics,QuestionCount):
        threshold = QuestionCount*100;
        '''temp = self.network.Calculate([1,1]);
        temp[11]=1;
        t1 = [i for i in temp];
        t1[9]=1;#Basics-units and dimensions
        t1[8]=1;#Units
        t1[25]=1;#Basics-laws of motion
        t1[24]=1;#Second law
        #print("temp: {}".format(t1));
        for t in range(0,70):
            self.network.Train([[1,1]], [t1], 1);
        self.desiredOutput=self.network.Calculate([1,1]);
        print("DesOutput: {}".format(self.desiredOutput));'''
        #print (threshold);
        EffectList = [];#[[TopicSheetIndex,EffectCount(Absolute value and not percentage)]]
        total =0;
        for i in range(0,len(Topics)):
            total+= self.desiredOutput[Topics[i][1]-1];
        for i in range(0,len(Topics)):
            EffectList.append([Topics[i][1],((self.desiredOutput[Topics[i][1]-1])/total)*threshold]);
            #[i][1] is the sheet index
        #print (EffectList);
        self.Phyquestions =[];
        self.Phyquestions=self.genQuestions(EffectList,QuestionCount);
    def genQuestions(self,EffectList,Qcount):
        templistE = [];
        Questions = [];
        a = int(self.getChapterAndTopic(EffectList[0][0])[0]);
        b=1;
        for i in range(0,len(EffectList)):
            b = int(self.getChapterAndTopic(EffectList[i][0])[0]);
            if(b!=a):
                if(i==0): b=a;
                else:
                    s=0;
                    for te in range(len(templistE)):
                            s+= templistE[te][1];
                    Questions.append(self.processQuestions(templistE, a,(s/(Qcount*100)*Qcount)));
                    a = int(self.getChapterAndTopic(EffectList[i][0])[0]);
                    templistE= [];
            if (a==b):
                templistE.append(EffectList[i]);
            if(i==len(EffectList)-1):
                s=0;
                for te in range(len(templistE)):
                    s+= templistE[te][1];
                Questions.append(self.processQuestions(templistE, b,(s/(Qcount*100)*Qcount)));
        return Questions;
                
    def processQuestions(self,tempList,Chapter,Qnum):
        QSheet = drive.sheet(self.auth,(str(Chapter)+"f"));
        TaggedQuestions=[];#Stores actual sheet index values of questions
        ActualQuestions=[];
        if(Qnum%int(Qnum)>0.5):Qnum=int(Qnum)+1;
        else: Qnum = int(Qnum)-1;#Confusion: Value-column-numbers etc.... algorythm = correct
        for i in range(0,len(tempList)):
            TopicValues=QSheet.getColumn(int(self.getChapterAndTopic(tempList[i][0])[1])+2); 
            Curr_req= float(tempList[i][1])/Qnum;
            #print("Req: {}".format(Curr_req))
            for j in range(0,len(TopicValues)):
                if not(TopicValues[j].isdigit): continue;
                elif(TopicValues[j]==''):continue;
                elif(TopicValues[j]==' '): continue;
                k = float(TopicValues[j]);
                if ((abs(k-Curr_req)/Curr_req)*100<=70):
                    temp=((k-Curr_req)/Curr_req*100);
                    if(temp==abs(temp)):#positive value
                        if(temp>=30): continue;
                    elif(temp!=abs(temp)):#negative value
                        if(abs(temp)>150):continue;
                    TaggedQuestions.append(j+1);
                    #print("Tagged Question {} due to Topic in column number {}".format(j+1,int(self.getChapterAndTopic(tempList[i][0])[1])+2));
                    #print("value = {}, targetValue={}".format(k,Curr_req))
        #tagging questions complete,Now generating a final list
        count = Counter(self.shuffle(TaggedQuestions));
        topQ = count.most_common(Qnum);
        for i in range(0,len(topQ)):
            ActualQuestions.append(int(topQ[i][0]));
        return [Chapter,ActualQuestions];
    def getTopicSheetIndex(self,Chapter,TopicNumber):
        try:
            self.topicsheet
        except NameError:
            self.topicsheet = drive.sheet(self.auth,"Topic_Codes");
        temprow = self.topicsheet.getColumn(1);
        #print(temprow);
        for i in range(0,len(temprow)):
            #print("Chap: {}   Topic: {}".format(temprow[i].strip().split('-')[0],temprow[i].strip().split('-')[1]))
            if((temprow[i].strip().split('-')[0]==str(Chapter))&(temprow[i].strip().split('-')[1]==str(TopicNumber))):
                return i+1;
        return 0;
    def getChapterAndTopic(self,topicSheetIndex):
        temprow = self.topicsheet.getColumn(1);
        return temprow[topicSheetIndex-1].strip().split('-');
            
    def setupBlackList(self):
        tempblacklist=[];#[[chapter,SheetIndex]]
        for i in range(0,len(self.questions)):
            if(self.questions[i][2]==1):
                tempblacklist.append([self.questions[i][0],self.questions[i][1]]);
        return tempblacklist;
    def shuffle(self,x):
        y = x[:]
        random.shuffle(y)
        return y
    def setTopics(self,Chapters):
        if(Sbot.topicsheet==1):
            Sbot.topicsheet = drive.sheet(self.auth,"Topic_Codes");
        topicstemp = Sbot.topicsheet.getColumn(1);
        self.topics = [];#[[Topic,SheetIndex],[Topic,SheetIndex]]
        for i in range(0,len(topicstemp)):
            for c in range(0,len(Chapters)):
                if (int(topicstemp[i].strip('-')[0])==int(Chapters[c])):
                    self.topics.append([topicstemp[i],i+1]);
            
    def SetupNetwork(self):
        Topics= drive.sheet(self.auth,"Topic_Codes");
        self.network = net.NewNetwork([2,5,len(Topics.getColumn(1))]);
        Sbot.db = drive.sheet(self.auth,"UserDB");
        self.setupUserDB(self.user);
        
    def setupUserDB(self,username):
        users = Sbot.db.getColumn(1);
        userpos =0;
        for i in range(0,len(users)):
            if(users[i]==username):
                userpos=i;
                self.questions = ast.literal_eval(Sbot.db.getCell(2,userpos+1));
                temp = self.network;
                temp.importWeights(Sbot.db.getCell(3,userpos+1));
                if(temp.OUTPUT_SIZE==self.network.OUTPUT_SIZE):
                    self.network.importWeights(Sbot.db.getCell(3,userpos+1));
                #print("in if part{}".format(self.network.Calculate([0,0])));
                break;
            elif(i==len(users)-1):
                userpos=len(users);
                Sbot.db.updateCell(1,userpos+1,username);
                Sbot.db.updateCell(2,userpos+1,"[]");
                for i in range(0,300):
                    self.network.Train([[1,1]],[self.network.OneDList(self.network.OUTPUT_SIZE)],0.5);
                Sbot.db.updateCell(3,userpos+1,str(self.network.getWeights()));
                self.questions = ast.literal_eval(Sbot.db.getCell(2,userpos+1));
                self.network.importWeights(Sbot.db.getCell(3,userpos+1));
                #print("in else part{}".format(self.network.Calculate([0,0])));
        self.userSheetIndex = userpos+1;        
    def Login(self,username,password):
        loginsheet= drive.sheet(self.auth,"User-Pass");
        users = loginsheet.getColumn(1);
        for i in range(0,len(users)):
            if(users[i].strip()==username):
                if(loginsheet.getCell(2, i+1)==password):
                    print ("Logged in successfully as {}".format(username));
                    self.user = username;
                    self.LOGIN_STATUS=1;
                    return;
                else:
                    print("incorrect password!");
                    self.LOGIN_STATUS=0;
                    return;
            elif(i==len(users)-1):
                print("Account not found! Create account (creating for now by default!)");
                loginsheet.updateCell(1, len(users)+1, username);
                loginsheet.updateCell(2,len(users)+1,password);
                self.user = username;
                self.LOGIN_STATUS=1;
                return;
    def readQuestion(self,Question):
        Question = Question.strip();
        QEnd=Question.find(" O:",0,len(Question));
        a = Question[:QEnd].strip();#a is the question
        b = Question[QEnd+3:];
        OA = b[b.find("(a)")+3:b.find("(b)")].strip();
        OB = b[b.find("(b)")+3:b.find("(c)")].strip();
        OC = b[b.find("(c)")+3:b.find("(d)")].strip();
        OD = b[b.find("(d)")+3:len(b)].strip();
        print("Q: {},     A:{},    B:{} ,    C:{},    D:{}".format(a,OA,OB,OC,OD));
user = Sbot("raunak114","LjPHceUR");
user.StartSession([1,4],8);
print (user.topics);