# **0x00. AirBnB clone - The console**

---
## This is the first fullstack project as ALX student

| Contents      | Details                                                                              |
|---------------|--------------------------------------------------------------------------------------|
| models        | Contains all the models for the projects<br/>BaseModel, User, City, State, Review... |
| models/engine | Contains the storage system for the project                                          |
| tests         | Contains all the unittests files for the project  

## More Details:
`the contents of that project are:`

* BaseModel - to take care of the initialization, serialization and deserialization of your future instances
* a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* (User, State, City, Place…) all classes in the project inherit from BaseModel
* the first abstracted storage engine of the project: File storage.
* unittests to validate all our classes and storage engine
