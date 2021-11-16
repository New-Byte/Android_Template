# import Modules
from Omegalib.omega import Omega,AppView,Buttons,TextField

# Create app
app = Omega()

# Create view
view = AppView(app=app)

# Write welcome msg
view.TextView(**{"android:id":"@+id/textView","android:layout_width":"wrap_content","android:layout_height":"wrap_content","android:text":"Welcome to Omega","android:textColor":"#148CDA", "app:layout_constraintBottom_toBottomOf":"parent","app:layout_constraintLeft_toLeftOf":"parent","app:layout_constraintRight_toRightOf":"parent","app:layout_constraintTop_toTopOf":"parent"}) 

# Run app
app.run()