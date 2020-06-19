from django.urls import path 
from api_app import views

urlpatterns = [
    path('',views.apiOverview,name="api-overview"),
     path('task-list/',views.taskList,name="task-list"),
      path('task-detail/<str:tid>/',views.taskDetail,name="task-detail"),
      path('task-create/',views.taskCreate,name="task-create"),#in this url u have to write a json value as below for respective id 
      
                                                                            #     {

                                                                            # "id":" 1",
                                                                            # "title":"Nirmal is awesome",
                                                                            # "completed":"True"
                                                                            # }
                                                                            
         path('task-update/<str:tid>/',views.taskUpdate,name="task-update"),
          path('task-delete/<str:tid>/',views.taskDelete,name="task-delete"),
]
