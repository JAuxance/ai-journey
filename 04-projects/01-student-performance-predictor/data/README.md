# Dataset of Student Performance Factors

## Dataset Description

This dataset contains information about students and their academic performance.

## Variables

| Column | Description | Type |
|---|---|---|
| `Hours Studied` | Study hours per week | Numerical |
| `Attendance` | Class attendance rate | Numerical |
| `Access to Resources` | Access to learning resources | Categorical |
| `Extracurricular Activities` | Participation in extracurricular activities | Categorical |
| `Sleep Hours` | Hours of sleep per night | Numerical |
| `Previous Scores` | Score from the previous year | Numerical |
| `Motivation Level` | Motivation level | Categorical |
| `Internet Access` | Internet access | Categorical |
| `Tutoring Sessions` | Number of tutoring sessions | Numerical |
| `Family Income` | Household income | Categorical |
| `Teacher Quality` | Quality of teaching | Categorical |
| `School Type` | Type of school (Public / Private) | Categorical |
| `Peer Influence` | Influence of peers (Positive / Negative) | Categorical |
| `Learning Disabilities` | Presence of learning disabilities | Categorical |
| `Parental Education Level` | Parents' education level | Categorical |
| `Distance from Home` | Distance between home and school | Categorical |
| `Gender` | Student gender | Categorical |
| `Exam Score` | **Final exam score (target)** | Numerical |

## Notes

- **Categorical** columns will require encoding (`get_dummies`) before training.
- The target variable is `Exam Score` — usable for regression (score) or classification (pass / fail).
