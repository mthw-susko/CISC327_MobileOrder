class ViewManager:
    def __init__(self):
        self.currentView = None
        self.nextView = None

    def changeView(self, view):
        # TODO: add validation to make sure the view given is a valid view
        self.nextView = view
        self.redirectToNextView()

    def redirectToNextView(self):
        if self.nextView is not None:
            self.currentView = self.nextView
            self.nextView = None
            print(f"Redirecting to {self.currentView.name} page.")
            self.currentView.viewApp()
        else:
            print("No page to redirect to.")
