import gspread
from oauth2client.service_account import ServiceAccountCredentials

class auth():
    def __init__(self,json_name):
        self.scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'];
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(json_name, self.scope);
        self.client = gspread.authorize(self.creds);
class sheet():
    def __init__(self,auth,sheetname):
        self.sheet = auth.client.open(sheetname).sheet1;
    def getSheet(self):
        return self.sheet;
    def switchSheet(self,newSheetName):
        self.sheet=auth.client.open(newSheetName).sheet1;
    def getColumn(self,index):
        return self.sheet.col_values(index);
    def getRow(self,index):
        return self.sheet.row_values(index);
    def getCell(self,X,Y):
        return self.sheet.cell(Y,X).value;
    def updateCell(self,X,Y,Value):
        self.sheet.update_cell(Y,X,Value);


#a = auth('client_secret.json');
#sheet1 = sheet(a,"Topic_Codes");
#print(sheet1.updateCell(3, 1, "this is a test"));   