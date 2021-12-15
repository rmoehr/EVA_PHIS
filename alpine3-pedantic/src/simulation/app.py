import model
import view
import controller

if __name__ == "__main__":
    model = model.Model()
    controller = controller.Controller(model)
    view = view.View(model, controller)
    controller.set_view(view)
    controller.update()
    view.mainloop()
