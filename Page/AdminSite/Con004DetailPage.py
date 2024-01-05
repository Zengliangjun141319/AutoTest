from operater import Operater

class Con004DetailPage(Operater):
    # Summary页元素
    ExpButton_loc = ('xpath', '//*[@id="nav_arrow"]/div')
    CommentsInputBox_loc = ('id', 'dialog_comments')
    CommitComments_loc = ('xpath', '//*[@id="div_comments"]/div[1]/table/tbody/tr[2]/td/div/div/span')
    # CommitComments_loc = ('class name', 'spanbtn iconsend')

    SaveButton_loc = ('xpath', '//*[@id="div_functionbar"]/input[1]')
    RefreshButton_loc = ('xpath', '//*[@id="div_functionbar"]/input[2]')

    # //*[@id="divcomments"]/div[1]/div[2]
    CommentResult_loc = ('xpath', '//*[@id="divcomments"]/div[1]/div[2]')

    locations_loc = ('id', 'nav_managelocations')

    Addlocation_loc = ('xpath', '//*[@id="content"]/div[2]/span[1]')
    locationnameinbox_loc = ('id', 'dialog_name')
    longinbox_loc = ('id', 'dialog_longitude')
    latinbox_loc = ('id', 'dialog_latitude')
    noteinbox_loc = ('id', 'dialog_notes')

    locOkbutton_loc = ('xpath', '//*[@id="dialog_location"]/div[4]/input[2]')
    addlocationresult_loc = ('xpath', '//*[@id="locationlist"]/div/div/div/table/tbody/tr[1]/td[1]/span')

    def inputTo(self, locator, Txt):
        self.send_keys(locator, Txt)