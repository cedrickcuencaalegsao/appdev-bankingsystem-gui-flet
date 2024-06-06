import flet
from flet import *

accountList = [
    {"account_number": 12345, "name": "Alice", "balance": 0},
    {"account_number": 67890, "name": "Bob", "balance": 0},
    {"account_number": 54321, "name": "Charlie", "balance": 0}
]
transactionList = []


class mainContent(UserControl):
    def __init__(self)->None:
        self.title = "Banking System - Python"
        
        self.count_acc = len(accountList)
        
        self.body = Container(
            border_radius=15,
            height=600,
            width=1000,
            padding=padding.only(left=15, top=25, right=15, bottom=10),
            clip_behavior=ClipBehavior.HARD_EDGE,
        )
        
        self.landing_page=Container(
            width=700,
            height=480,
            margin=margin.only(left=15, right=0, top=-5, bottom=0),
            bgcolor="white",
            border_radius=15,
            animate=animation.Animation(300, "decelerate"),
            content=Container(
                content=Column(
                    controls=[
                        self.landingPage(), 
                    ]
                )
            )
        )
        
        self.home=Container(
            width=0,
            height=480,
            margin=margin.only(left=0, right=0, top=-5, bottom=0),
            bgcolor=None,
            alignment=alignment.center,
            border_radius=15,
            animate=animation.Animation(300, "decelerate"),
            content=Container(
                content=Column(
                    controls=[
                        self.homeControls(), 
                    ]
                )
            )
        )
        self.create_Acc=Container(
            width=0,
            height=480,
            margin=margin.only(left=0, right=0, top=-5, bottom=0),
            bgcolor=None,
            alignment=alignment.center,
            border_radius=15,
            animate=animation.Animation(300, "decelerate"),
            content=Container(
                content=Column(
                    controls=[
                        self.creatAcc(), 
                    ]
                )
            )
        )
        self.login_acc=Container(
            width=0,
            height=480,
            margin=margin.only(left=0, right=0, top=-5, bottom=0),
            bgcolor=None,
            alignment=alignment.center,
            border_radius=15,
            animate=animation.Animation(300, "decelerate"),
            content=Container(
                content=Column(
                    controls=[
                        self.loginAcc(), 
                    ]
                )
            )
        )
        self.display_acc=Container(
            width=0,
            height=480,
            margin=margin.only(left=0, right=0, top=-5, bottom=0),
            bgcolor=None,
            alignment=alignment.center,
            border_radius=15,
            animate=animation.Animation(300, "decelerate"),
            content=Container(
                content=Column(
                    controls=[
                        self.displayAllAcc(), 
                    ]
                )
            )
        )
        self.history=Container(
            width=0,
            height=480,
            margin=margin.only(left=0, right=0, top=-5, bottom=0),
            bgcolor="#02367b",
            alignment=alignment.center,
            border_radius=15,
            animate=animation.Animation(300, "decelerate"),
        )
        self.best_acc=Container(
            width=0,
            height=480,
            margin=margin.only(left=0, right=0, top=-5, bottom=0),
            bgcolor="#02367b",
            alignment=alignment.center,
            border_radius=15,
            animate=animation.Animation(300, "decelerate"),
        )
        self.vip_acc=Container(
            width=0,
            height=480,
            margin=margin.only(left=0, right=0, top=-5, bottom=0),
            bgcolor="#02367b",
            alignment=alignment.center,
            border_radius=15,
            animate=animation.Animation(300, "decelerate"),
        )
        self.remove_acc=Container(
            width=0,
            height=480,
            margin=margin.only(left=0, right=0, top=-5, bottom=0),
            bgcolor="#02367b",
            alignment=alignment.center,
            border_radius=15,
            animate=animation.Animation(300, "decelerate"),
        )
        self.update_acc=Container(
            width=0,
            height=480,
            margin=margin.only(left=0, right=0, top=-5, bottom=0),
            bgcolor="#02367b",
            alignment=alignment.center,
            border_radius=15,
            animate=animation.Animation(300, "decelerate"),
        )
        
        self.main_stack = Stack()
        
        super().__init__()
    
    def hoverMenu(self, e):
        if e.data == 'true':
            e.control.bgcolor = '#e5ebfb'
            e.control.update()
            
            e.control.content.controls[0].icon_color = '#006ca5'
            e.control.content.controls[1].color = '#006ca5'
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()
            
            e.control.content.controls[0].icon_color = '#02367b'
             
            e.control.content.controls[1].color = '#02367b'
            e.control.content.update() 
    
    def landingPage(self):
        return Container(
            content=Column(
                controls=[
                    Container(
                        margin=margin.only(top=15, left=15),
                        content=Column(
                            controls=[
                                Container(
                                    width=700,
                                    margin=margin.only(left=230),
                                    content=Row(
                                        controls=[
                                            Text(
                                                "System Stats.",
                                                color="#264d59",
                                                size=30,
                                                weight="w700",
                                            )
                                        ]
                                    )
                                ),
                                Container(
                                    content=Row(
                                        controls=[
                                            Text(
                                                "Regestered Account.",
                                                color="#264d59",
                                                size=20,
                                                weight="w700",
                                            ),
                                            Text(
                                                self.count_acc,
                                                size=15,
                                                color="#000000",
                                                weight="w700",
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
    
    def homeControls(self):
        return Container(
            margin=margin.only(left=15),
            content=Column(
                controls=[
                    Container(
                        alignment=alignment.center,
                        content=Text(
                            "Home",
                            color="#264d59",
                            size=40,
                            weight="w700",
                        )
                    ),
                    Row(
                        controls=[
                            Container(
                                width=300,
                                margin=margin.only(left=100, right=0, top=35),
                                content=Column(
                                    controls=[
                                        Row(
                                            controls=[
                                                Icon(
                                                    name=icons.CHECK,
                                                    color="#264d59",
                                                ),
                                                Text(
                                                    "Create Accont",
                                                    size=18,
                                                    color="#264d59",
                                                    weight="w700",
                                                ),
                                                
                                            ]
                                        ),
                                        Row(
                                            controls=[
                                                Icon(
                                                    name=icons.CHECK,
                                                    color="#264d59",
                                                ),
                                                Text(
                                                    "Login",
                                                    size=18,
                                                    color="#264d59",
                                                    weight="w700",
                                                ),
                                            ]
                                        ),
                                        Row(
                                            controls=[
                                                Icon(
                                                    name=icons.CHECK,
                                                    color="#264d59",
                                                ),
                                                Text(
                                                    "Display All Account",
                                                    size=18,
                                                    color="#264d59",
                                                    weight="w700",
                                                ),
                                            ]
                                        ),
                                        Row(
                                            controls=[
                                                Icon(
                                                    name=icons.CHECK,
                                                    color="#264d59",
                                                ),
                                                Text(
                                                    "Transaction Logs",
                                                    size=18,
                                                    color="#264d59",
                                                    weight="w700",
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                            Container(
                                width=300,
                                margin=margin.only(left=0, right=0, top=35),
                                content=Column(
                                    controls=[
                                        Row(
                                            controls=[
                                                Icon(
                                                    name=icons.CHECK,
                                                    color="#264d59",
                                                ),
                                                Text(
                                                    "Best Account",
                                                    size=18,
                                                    color="#264d59",
                                                    weight="w700",
                                                )
                                            ],
                                        ),
                                        Row(
                                            controls=[
                                                Icon(
                                                    name=icons.CHECK,
                                                    color="#264d59",
                                                ),
                                                Text(
                                                    "VIP Account",
                                                    size=18,
                                                    color="#264d59",
                                                    weight="w700",
                                                )
                                            ],
                                        ),
                                        Row(
                                            controls=[
                                                Icon(
                                                    name=icons.CHECK,
                                                    color="#264d59",
                                                ),
                                                Text(
                                                    "Remove Account",
                                                    size=18,
                                                    color="#264d59",
                                                    weight="w700",
                                                )
                                            ],
                                        ),
                                        Row(
                                            controls=[
                                                Icon(
                                                    name=icons.CHECK,
                                                    color="#264d59",
                                                ),
                                                Text(
                                                    "Update Account",
                                                    size=18,
                                                    color="#264d59",
                                                    weight="w700",
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                        ]
                    ),
                    
                ]
            ),
        )
        
    def creatAcc(self):
        return Container(
            width=700,
            height=480,
            margin=margin.only(left=5),
            content=Column(
                controls=[
                    Container(
                        alignment=alignment.center,
                        content=Text(
                            "Create Account",
                            color="#264d59",
                            size=40,
                            weight="w700",
                        )
                    ),
                    Row(
                        controls=[
                            Container(
                                width=330,
                                alignment=alignment.center,
                                content=Column(
                                    controls=[
                                        TextField(
                                            label="Account Name",
                                            label_style=TextStyle(
                                                color="#264d59",
                                                weight="w700",
                                                size=20,
                                                ),
                                            border_radius=10,
                                            border_color="#000000",
                                            focused_border_color=colors.ORANGE_700,
                                            text_style=TextStyle(
                                                color="#000000",
                                            ),
                                        ),
                                        TextField(
                                            label="Account Type",
                                            label_style=TextStyle(
                                                color="#264d59",
                                                weight="w700",
                                                size=20,
                                            ),
                                            border_radius=10,
                                            border_color="#000000",
                                            focused_border_color=colors.ORANGE_700,
                                            text_style=TextStyle(
                                                color="#000000",
                                            ),
                                        ),
                                    ],
                                ),
                                
                            ),
                            Container(
                                width=330,
                                alignment=alignment.center,
                                content=Column(
                                    controls=[
                                        TextField(
                                            label="Gender",
                                            label_style=TextStyle(
                                                color="#264d59",
                                                weight="w700",
                                                size=20,
                                            ),
                                            border_radius=10,
                                            border_color="#000000",
                                            focused_border_color=colors.ORANGE_700,
                                            text_style=TextStyle(
                                                color="#000000",
                                            ),
                                        ),
                                        TextField(
                                            label="Address",
                                            label_style=TextStyle(
                                                color="#264d59",
                                                weight="w700",
                                                size=20,
                                            ),
                                            border_radius=10,
                                            border_color="#000000",
                                            focused_border_color=colors.ORANGE_700,
                                            text_style=TextStyle(
                                                color="#000000",
                                            ),
                                        ),
                                    ]
                                )
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            Container(
                                content=ElevatedButton(
                                    text="Create",
                                    height=50,
                                    width=330,
                                    style=ButtonStyle(
                                        color="#ffffff",
                                        bgcolor="#f9ad6a",
                                        shape={
                                            MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
                                            MaterialState.FOCUSED: RoundedRectangleBorder(radius=15),
                                            MaterialState.HOVERED: RoundedRectangleBorder(radius=15),
                                        }
                                    )
                                )
                            ),
                            Container(
                                content=ElevatedButton(
                                    text="Cancel",
                                    height=50,
                                    width=330,
                                    style=ButtonStyle(
                                        color="#ffffff",
                                        bgcolor="#d46c4e",
                                        shape={
                                            MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
                                            MaterialState.FOCUSED: RoundedRectangleBorder(radius=15),
                                            MaterialState.HOVERED: RoundedRectangleBorder(radius=15),
                                        }
                                    )
                                )
                            ),
                        ]
                    )
                ]
            ),
        )
    
    def loginAcc(self):
        login_acc = Container(
            width=700,
            height=480,
            margin=margin.only(left=5),
            content=Column(
                controls=[
                    Container(
                        alignment=alignment.center,
                        content=Column(
                            controls=[
                                Text(
                                    "Login",
                                    color="#264d59",
                                    size=40,
                                    weight="w700",
                                ),
                                
                            ]
                        )
                    ),
                    Container(
                        margin=margin.only(top=10),
                        alignment=alignment.center,
                        content=Column(
                            controls=[
                                TextField(
                                    label="Account Number",
                                    width=300,
                                    label_style=TextStyle(
                                        color="#264d59",
                                        weight="w700",
                                        size=20,
                                    ),
                                    border_radius=10,
                                    border_color="#000000",
                                    focused_border_color=colors.ORANGE_700,
                                    text_style=TextStyle(
                                        color="#000000",
                                    ),
                                ),
                                ElevatedButton(
                                    text="Login",
                                    height=50,
                                    width=300,
                                    style=ButtonStyle(
                                        color="#ffffff",
                                        bgcolor="#f9ad6a",
                                        shape={
                                            MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
                                            MaterialState.FOCUSED: RoundedRectangleBorder(radius=15),
                                            MaterialState.HOVERED: RoundedRectangleBorder(radius=15),
                                        }
                                    )
                                ),
                            ]
                        )
                    )
                ]
            )
        )
        
        err_acc = Container(
            alignment=alignment.center,
            content=Column(
                controls=[
                    Container(
                        content=Text(
                                "No Account Registered - 404 ",
                                color="red",
                                weight="W600",
                                size=40,
                        )
                    ),
                ]
            )
        )
        
        count = len(accountList)
        
        if count != 0: 
            return login_acc
        else:
            return err_acc
    
    def displayAllAcc(self):
        
        err_no_registers_acc = Container(
            width=700,
            margin=margin.only(left=50, top=10),
            content=Row(
                controls=[
                    Container(
                        content=Text(
                            "No Account Found! - 404",
                            size=40,
                            color="red",
                            weight="w700",
                        ),
                    )
                ]
            )
        )
        display_all_acc = Container(
            content=Column(
                controls=[
                    Container(
                        content=Text(
                            "Display All Account.",
                            color="#02367b",
                            size=40,
                            weight="w700",
                        )
                    ),
                    
                ]
            )
        )
        if self.count_acc != 0:
            return display_all_acc
        else:
            return err_no_registers_acc
        
    def showView(self, viewName):
        if viewName == 'Home':
            if self.home.width == 0:
                
                self.landing_page.width = 0
                self.landing_page.update()
                
                self.home.width = 700
                self.create_Acc.width = 0
                self.login_acc.width = 0
                self.display_acc.width = 0
                self.history.width = 0
                self.best_acc.width = 0
                self.vip_acc.width = 0
                self.remove_acc.width = 0
                self.update_acc.width = 0
                
                self.home.update()
                self.create_Acc.update()
                self.login_acc.update()
                self.display_acc.update()
                self.history.update()
                self.best_acc.update()
                self.vip_acc.update()
                self.remove_acc.update()
                self.update_acc.update()
            else:
                self.home.width = 0
                self.home.update()

                self.landing_page.width = 700
                self.landing_page.update()
            
        if viewName == 'Create Account':
            if self.create_Acc.width == 0:
                
                self.landing_page.width = 0
                self.landing_page.update()
                
                self.home.width = 0
                self.create_Acc.width = 700
                self.login_acc.width = 0
                self.display_acc.width = 0
                self.history.width = 0
                self.best_acc.width = 0
                self.vip_acc.width = 0
                self.remove_acc.width = 0
                self.update_acc.width = 0
                
                self.home.update()
                self.create_Acc.update()
                self.login_acc.update()
                self.display_acc.update()
                self.history.update()
                self.best_acc.update()
                self.vip_acc.update()
                self.remove_acc.update()
                self.update_acc.update()
            else:
                self.create_Acc.width = 0
                self.create_Acc.update()
                
                self.landing_page.width = 700
                self.landing_page.update()
        
        if viewName == 'Login':
            if self.login_acc.width == 0:
                
                self.landing_page.width = 0
                self.landing_page.update()
                
                self.home.width = 0
                self.create_Acc.width = 0
                self.login_acc.width = 700
                self.display_acc.width = 0
                self.history.width = 0
                self.best_acc.width = 0
                self.vip_acc.width = 0
                self.remove_acc.width = 0
                self.update_acc.width = 0
                
                self.home.update()
                self.create_Acc.update()
                self.login_acc.update()
                self.display_acc.update()
                self.history.update()
                self.best_acc.update()
                self.vip_acc.update()
                self.remove_acc.update()
                self.update_acc.update()
            else:
                self.login_acc.width = 0
                self.login_acc.update()
                
                self.landing_page.width = 700
                self.landing_page.update()
                
        if viewName == 'All Account':
            if self.display_acc.width == 0:
                
                self.landing_page.width = 0
                self.landing_page.update()
                
                self.home.width = 0
                self.create_Acc.width = 0
                self.login_acc.width = 0
                self.display_acc.width = 700
                self.history.width = 0
                self.best_acc.width = 0
                self.vip_acc.width = 0
                self.remove_acc.width = 0
                self.update_acc.width = 0
                
                self.home.update()
                self.create_Acc.update()
                self.login_acc.update()
                self.display_acc.update()
                self.history.update()
                self.best_acc.update()
                self.vip_acc.update()
                self.remove_acc.update()
                self.update_acc.update()
            else:
                self.display_acc.width = 0
                self.display_acc.update()
                
                self.landing_page.width = 700
                self.landing_page.update()
        
        if viewName == 'History':
            if self.history.width == 0:
                
                self.landing_page.width = 0
                self.landing_page.update()
                
                self.home.width = 0
                self.create_Acc.width = 0
                self.login_acc.width = 0
                self.display_acc.width = 0
                self.history.width = 700
                self.best_acc.width = 0
                self.vip_acc.width = 0
                self.remove_acc.width = 0
                self.update_acc.width = 0
                
                self.home.update()
                self.create_Acc.update()
                self.login_acc.update()
                self.display_acc.update()
                self.history.update()
                self.best_acc.update()
                self.vip_acc.update()
                self.remove_acc.update()
                self.update_acc.update()
            else:
                self.history.width = 0
                self.history.update()
                
                self.landing_page.width = 700
                self.landing_page.update()
                
        if viewName == 'Best Account':
            
            if self.best_acc.width == 0:
                
                self.landing_page.width = 0
                self.landing_page.update()
                
                self.home.width = 0
                self.create_Acc.width = 0
                self.login_acc.width = 0
                self.display_acc.width = 0
                self.history.width = 0
                self.best_acc.width = 700
                self.vip_acc.width = 0
                self.remove_acc.width = 0
                self.update_acc.width = 0
                
                self.home.update()
                self.create_Acc.update()
                self.login_acc.update()
                self.display_acc.update()
                self.history.update()
                self.best_acc.update()
                self.vip_acc.update()
                self.remove_acc.update()
                self.update_acc.update()
            else:
                self.best_acc.width = 0
                self.best_acc.update()
                
                self.landing_page.width = 700
                self.landing_page.update()
            
        if viewName == 'VIP Account':
            if self.vip_acc.width == 0:
                
                self.landing_page.width = 0
                self.landing_page.update()
                
                self.home.width = 0
                self.create_Acc.width = 0
                self.login_acc.width = 0
                self.display_acc.width = 0
                self.history.width = 0
                self.best_acc.width = 0
                self.vip_acc.width = 700
                self.remove_acc.width = 0
                self.update_acc.width = 0
                
                self.home.update()
                self.create_Acc.update()
                self.login_acc.update()
                self.display_acc.update()
                self.history.update()
                self.best_acc.update()
                self.vip_acc.update()
                self.remove_acc.update()
                self.update_acc.update()
            else:
                self.vip_acc.width = 0
                self.vip_acc.update()
                
                self.landing_page.width = 700
                self.landing_page.update()
                
        if viewName == 'Remove Account':
            if self.remove_acc.width == 0:
                
                self.landing_page.width = 0
                self.landing_page.update()
                
                self.home.width = 0
                self.create_Acc.width = 0
                self.login_acc.width = 0
                self.display_acc.width = 0
                self.history.width = 0
                self.best_acc.width = 0
                self.vip_acc.width = 0
                self.remove_acc.width = 700
                self.update_acc.width = 0
                
                self.home.update()
                self.create_Acc.update()
                self.login_acc.update()
                self.display_acc.update()
                self.history.update()
                self.best_acc.update()
                self.vip_acc.update()
                self.remove_acc.update()
                self.update_acc.update()
            else:
                self.remove_acc.width = 0
                self.remove_acc.update()
                
                self.landing_page.width = 700
                self.landing_page.update()
            
        if viewName == 'Update Account':
            if self.update_acc.width == 0:
                
                self.landing_page.width = 0
                self.landing_page.update()
                
                self.home.width = 0
                self.create_Acc.width = 0
                self.login_acc.width = 0
                self.display_acc.width = 0
                self.history.width = 0
                self.best_acc.width = 0
                self.vip_acc.width = 0
                self.remove_acc.width = 0
                self.update_acc.width = 700
                
                self.home.update()
                self.create_Acc.update()
                self.login_acc.update()
                self.display_acc.update()
                self.history.update()
                self.best_acc.update()
                self.vip_acc.update()
                self.remove_acc.update()
                self.update_acc.update()
            else:
                self.landing_page.width = 700
                self.landing_page.update()
                
                self.update_acc.width = 0
                self.update_acc.update()
                
    def menuClicked(self, text):
        if str(text) == 'Home':
            self.showView(viewName=text)
        elif str(text) == 'Create Account':
            self.showView(viewName=text)
        elif str(text) == 'Login':
            self.showView(viewName=text)
        elif str(text) == 'All Account':
            self.showView(viewName=text)
        elif str(text) == 'History':
            self.showView(viewName=text)
        elif str(text) == 'Best Account':
            self.showView(viewName=text)
        elif str(text) == 'VIP Account':
            self.showView(viewName=text)
        elif str(text) == 'Remove Account':
            self.showView(viewName=text)
        elif str(text) == 'Update Account':
            self.showView(viewName=text)

    def sideBarIcon(self, icon_name:str, text:str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            margin=margin.only(left=5, right=5, top=0),
            on_click=lambda e: self.menuClicked(text),
            on_hover=lambda e: self.hoverMenu(e),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=30,
                        icon_color="#02367b",
                        style=ButtonStyle(
                            shape={
                                "":RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={
                                "": "transparent"  
                            },
                        )
                    ),
                    Text(
                        value=text,
                        color="#02367b",
                        size=15,
                        opacity=1,
                        animate_opacity=200,
                        weight="w700",
                    )
                ]
            ),
        )
        
    def build(self):
        items: list = [
            Column(
                controls=[
                    #title
                    Container(
                        width=700,
                        height=50,
                        margin=margin.only(left=230, top=-20),
                        content=Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                Text(
                                    self.title,
                                    color="#02367b",
                                    weight="w900",
                                    size=30,
                                ),
                            ],
                        ),
                    ),
                    Row(
                        #sidebar
                        controls=[
                            Container(
                                alignment=alignment.center,
                                width=200,
                                height=550,
                                margin=margin.only(top=-50, left=-5),
                                border_radius=15,
                                content=Column(
                                    controls=[
                                        Container(
                                            margin=margin.only(left=15, top=10),
                                            content=Row(
                                                controls=[
                                                    Icon(
                                                        name=icons.MENU_ROUNDED,
                                                        color="#02367b",
                                                        size=40,
                                                    ),
                                                    Text(
                                                        "Main Menu",
                                                        weight="w700",
                                                        size=20,
                                                        color="#02367b",
                                                    ),
                                                ]
                                            )
                                        ),
                                        self.sideBarIcon(icons.HOME_ROUNDED,"Home"),
                                        self.sideBarIcon(icons.CREATE_ROUNDED , "Create Account"),
                                        self.sideBarIcon(icons.LOGIN_ROUNDED , "Login"),
                                        self.sideBarIcon(icons.LIST_ALT_ROUNDED, "All Account"),
                                        self.sideBarIcon(icons.HISTORY_ROUNDED , "History"),
                                        self.sideBarIcon(icons.BAR_CHART_ROUNDED , "Best Account"),
                                        self.sideBarIcon(icons.WORKSPACE_PREMIUM_ROUNDED , "VIP Account"),
                                        self.sideBarIcon(icons.DELETE_ROUNDED , "Remove Account"),
                                        self.sideBarIcon(icons.UPDATE_ROUNDED , "Update Account"),
                                    ]
                                )
                            ),
                            # Body dislay
                            self.landing_page,
                            self.home,
                            self.create_Acc,
                            self.login_acc,
                            self.display_acc,
                            self.history,
                            self.best_acc,
                            self.vip_acc,
                            self.remove_acc,
                            self.update_acc,
                        ]
                    ),
                ]
            )
        ]
        
        self.main_stack.controls = items
        self.body.content = self.main_stack
        return self.body

def main(page: Page):
    page.window_center()
    page.title = "Banking System - Python"
    page.bgcolor = "#ffffff"
    page.window_width = 1000
    page.window_height = 625
    page.window_resizable = False
    
    main_content = mainContent()
    
    page.add(
        Stack(
            controls=[
                main_content
            ]
        )
    )
    
    page.update()
    
if __name__ == "__main__":
    flet.app(target=main)