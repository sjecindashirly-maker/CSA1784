% Medical Diagnosis System

disease(fever, flu).
disease(cough, flu).
disease(headache, flu).

disease(fever, malaria).
disease(chills, malaria).
disease(sweating, malaria).

% Rule for diagnosis
diagnose(Symptom, Disease) :-
    disease(Symptom, Disease).
