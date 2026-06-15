% Disease and Diet Database

diet(diabetes, 'Low sugar diet').
diet(hypertension, 'Low salt diet').
diet(obesity, 'Low fat diet').
diet(anemia, 'Iron rich diet').
diet(heart_disease, 'Low cholesterol diet').

% Rule to suggest diet
suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).
