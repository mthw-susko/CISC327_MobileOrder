class ViewManager:
    def __init__(self):
        # Attributes
        self.currentView = None
        self.nextView = None

    def changeView(self, view):
        # Handles routing of views (abstraction)
        self.nextView = view
        self.redirectToNextView()

    def redirectToNextView(self):
        # Helper function that contains logic for routing
        if self.nextView is not None:
            self.currentView = self.nextView
            self.nextView = None
            print(f"Redirecting to {self.currentView.name} page.")
            self.currentView.viewApp()
        else:
            print("No page to redirect to.")
