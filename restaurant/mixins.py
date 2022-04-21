class BookTableMixin():
    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.user = self.request.user
        return super().form_valid(form)
