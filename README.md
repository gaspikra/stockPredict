Este fue mi primer proyecto para aplicar lo aprendido del libro "Aprende Machine Learning con Scikit-Learn, Keras y TensorFlow" de Aurélien Géron, en donde aprendí a tunear y entender un poco los hiperparámetros, "jugando" con ellos.

En primer lugar, experimenté con los hiperparámetros de los modelos, como los de las redes neuronales de Keras (L1, L2, Dropout), ya que encontrando la mejor combinación entre ellos, podés lograr que el modelo no memorice datos (overfit),
pero si la combinación es muy restrictiva, el modelo puede hacer underfitting. Por ejemplo, subir alpha en L2 para que el modelo no le dé tanta importancia a los outliers, pero si combinado a esto le sumás un Dropout alto, el modelo estaría siendo muy restringido,
entonces podés sumarle más neuronas a cada capa para que analice mejores patrones, o más epochs, para que recorra más veces el set de datos aprendiendo poco a poco. Con una combinación óptima, se puede lograr que el modelo no tenga overfit ni underfit y que este
converja a un punto óptimo.

En segundo lugar, entendí que la visualización de datos previo a iniciar a entrenar un modelo es fundamental, ya que de aquí podés obtener información muy valiosa, como por ejemplo, qué datos son solo ruido y no sirven, qué datos sí son importantes y no se relacionan 
entre ellos o la distribución de los datos (fundamental para elegir un modelo). Además, con la ingeniería de datos, agregando nuevas columnas al modelo (obviamente, que tengan impacto y sentido lógico) puede ser muy beneficioso; en este caso por ejemplo,
cuando añadí la distancia con las MM21 y MM50, se notó un impacto positivo en cuanto a la relación con otros datos e información que se le agrega al modelo.

Por último, descubrí que está bueno entrenar varios modelos, el primero cuanto más básico mejor, ya que va a actuar como una baseline para compararlo con otros modelos más complejos, y de aquí se puede obtener una conclusión final con mejores fundamentos.

En conclusión, luego de haber entrenado varios modelos, la diferencia con el primero NO es notoria; usé el LinearRegressor como baseline, pero los modelos más complejos no lograron romper significativamente esa barrera del MSE 0.0066 en el set de testeo,
por lo que en caso de tener que implementar sí o si un modelo, el mejor sería LinearRegression, por su costo de mantenimiento, utilización de recursos o explicabilidad, pero también habla de que el dataset no brinda información suficiente o tan relevante
como para poder tener predicciones más acertadas, por lo que buscar nuevos datos podría ser óptimo para obtener mejores resultados.
