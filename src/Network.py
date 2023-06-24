import random as r;
import math as math;
import ast;
class NewNetwork():
    def __init__(self,NetworkSizes):
        self.NETWORK_LAYER_SIZES = NetworkSizes;
        self.NETWORK_SIZE = len(self.NETWORK_LAYER_SIZES);
        self.INPUT_SIZE = self.NETWORK_LAYER_SIZES[0];
        self.OUTPUT_SIZE = self.NETWORK_LAYER_SIZES[self.NETWORK_SIZE-1];
        self.output = list();#[layer][neurons]
        self.weights = list();#[layer][neuron][prevNeuron]
        self.slopes = list();#[layer][neuron][prevNeuron][avglist]
        self.SetupLists();
    def Train(self,inputs,desOutputs,rate):
        if (len(inputs)!= len(desOutputs)): 
            print ("input and output sizes dont match!");
            return;
        for i in range(0,len(inputs)):
            if(len(inputs[i])!=self.INPUT_SIZE):
                print ("incorrect input size (input number) {}".format(i));
                return;
            if(len(desOutputs[i])!= self.OUTPUT_SIZE):
                print ("Incorrect output size (output number) {}".format(i));
        errors = self.OneDList(self.OUTPUT_SIZE);
        #print(desOutputs[i]);
        for layer in range(1,self.NETWORK_SIZE):
                for neuron in range(0,self.NETWORK_LAYER_SIZES[layer]):
                    for prevNeuron in range(0, self.NETWORK_LAYER_SIZES[layer-1]):
                        self.slopes[layer][neuron][prevNeuron] = self.OneDList(len(inputs));
        for i in range(0,len(inputs)):#reiteration
            tempOutput = self.Calculate(inputs[i]);
            for EC in range(0,self.OUTPUT_SIZE):
                errors[EC] = tempOutput[EC]-desOutputs[i][EC];
            #last layer
            for neuron in range(0,self.NETWORK_LAYER_SIZES[self.NETWORK_SIZE-1]):
                for prevNeuron in range(0,self.NETWORK_LAYER_SIZES[self.NETWORK_SIZE-2]):
                    self.slopes[self.NETWORK_SIZE-1][neuron][prevNeuron][i] = self.output[self.NETWORK_SIZE-2][prevNeuron]*self.output[self.NETWORK_SIZE-1][neuron]*(1-self.output[self.NETWORK_SIZE-1][neuron])*errors[neuron];
                #print(self.slopes[self.NETWORK_SIZE-1][neuron]);
            #last layer done
            
            Fsum =0;
            for layer in range(self.NETWORK_SIZE-2,0,-1):
                for neuron in range(0,self.NETWORK_LAYER_SIZES[layer]):
                    for prevNeuron in range(0,self.NETWORK_LAYER_SIZES[layer-1]):
                        for sumwt in range(0,self.NETWORK_LAYER_SIZES[layer+1]):
                            Fsum+= self.slopes[layer+1][sumwt][neuron][i]*self.weights[layer+1][sumwt][neuron];
                        self.slopes[layer][neuron][prevNeuron][i] = self.output[layer-1][prevNeuron]*(1-self.output[layer][neuron])*Fsum;
                        Fsum=0;
            #end of slope setting
        tempavg=0;
        for layer in range(1,self.NETWORK_SIZE):
            for neuron in range(0,self.NETWORK_LAYER_SIZES[layer]):
                for prevNeuron in range(0,self.NETWORK_LAYER_SIZES[layer-1]):
                    for avgcount in range(0,len(inputs)):
                        tempavg+=self.slopes[layer][neuron][prevNeuron][avgcount];
                    tempavg/=len(inputs);
                    #print ("Slope between neuron {0} of layer {1},and prevNeuron {2} of layer {3} is {4}".format(neuron,layer,prevNeuron,layer-1,tempavg))
                    self.weights[layer][neuron][prevNeuron]-=rate*tempavg;
                    tempavg=0;
                                            
    
    def addNeuron(self,Layer):
        if(Layer==self.NETWORK_SIZE-1):
            self.OUTPUT_SIZE+=1;
            self.NETWORK_LAYER_SIZES[self.NETWORK_SIZE-1]+=1;
            self.output[self.NETWORK_SIZE-1].append(0);
            self.weights[self.NETWORK_SIZE-1].append([0]);
            self.weights[self.NETWORK_SIZE-1][self.NETWORK_LAYER_SIZES[self.NETWORK_SIZE-1]-1] = self.OneDList(self.NETWORK_LAYER_SIZES[self.NETWORK_SIZE-2],1);
            self.slopes[self.NETWORK_SIZE-1].append([0]);
            self.slopes[self.NETWORK_SIZE-1][self.NETWORK_LAYER_SIZES[self.NETWORK_SIZE-1]-1] = self.OneDList(self.NETWORK_LAYER_SIZES[self.NETWORK_SIZE-2],1);
            #print (len(self.slopes[self.NETWORK_SIZE-1][self.NETWORK_LAYER_SIZES[self.NETWORK_SIZE-1]-1]));
            for prevNeuron in range(0,self.NETWORK_LAYER_SIZES[self.NETWORK_SIZE-2]):
                self.slopes[self.NETWORK_SIZE-1][self.NETWORK_LAYER_SIZES[self.NETWORK_SIZE-1]-1][prevNeuron]= list([]);
    def Calculate(self,inputs):#double array inputs
            if(len(inputs)!=self.INPUT_SIZE): 
                print ("Incorrect input size");
                return;
            self.output[0] = inputs;
            for layer in range(1,self.NETWORK_SIZE):
                for Neuron in range(0,self.NETWORK_LAYER_SIZES[layer]):
                    sum1 = 0;
                    for prevNeuron in range(0, self.NETWORK_LAYER_SIZES[layer-1]):
                        sum1+=self.output[layer-1][prevNeuron]*self.weights[layer][Neuron][prevNeuron];
                    self.output[layer][Neuron] = self.actiFunc(sum1);
            return self.output[self.NETWORK_SIZE-1];
    def actiFunc(self,inputi):
        output = 1/(1+math.e**(-inputi));
        return output;
    
    
    def EmptySlopes(self):
        self.slopes = list();
        for layer in range(self.NETWORK_SIZE):
            self.slopes.append(self.OneDList(self.NETWORK_LAYER_SIZES[layer], 0));
            if (layer>0):
                for Neuron in range(len(self.weights[layer])):
                    self.slopes[layer][Neuron] = self.OneDList(self.NETWORK_LAYER_SIZES[layer-1],1);
                    for prevNeuron in range(len(self.slopes[layer][Neuron])):
                        self.slopes[layer][Neuron][prevNeuron]= list(); 
    
    
    def SetupLists(self):
        for layer in range(self.NETWORK_SIZE):
            self.output.append(self.OneDList(self.NETWORK_LAYER_SIZES[layer]));
            self.weights.append(self.OneDList(self.NETWORK_LAYER_SIZES[layer], 0));
            if (layer>0):
                for Neuron in range(len(self.weights[layer])):
                    self.weights[layer][Neuron] = self.OneDList(self.NETWORK_LAYER_SIZES[layer-1],1);

            #[layer][neuron][prevNeuron][slopeList]
        self.EmptySlopes();    
    
    
    def OneDList(self,size,random=0):
        a1 = list([]);
        for i in range(0,size):
            if(random==0):
                a1.append(0);
            else:
                rNum = r.randint(-10000,10000)/10000;
                a1.append(rNum);
        return a1;
    def getWeights(self):
        return self.weights;
    def setWeights(self,weights):
        self.weights=weights;
    def importWeights(self,weightstr):
        self.weights = ast.literal_eval(weightstr);