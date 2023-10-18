class ViewManager:
    ''' Note!! View class has not been defined '''

    def __init__(self, currentView):
        self.currentView = currentView
        self.nextView = None

    def changeView(self, view):
        if isinstance(view, View):
            self.nextView = view
            self.redirectToNextView()
        else:
            print("Invalid page. Please provide a valid View object.")

    def redirectToNextView(self):
        if self.nextView is not None:
            self.currentView = self.nextView
            self.nextView = None
            print(f"Redirecting to {self.currentView.name} page.")
        else:
            print("No page to redirect to.")