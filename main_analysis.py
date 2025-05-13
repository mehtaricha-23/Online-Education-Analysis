import pandas as pd
import numpy as np



students = pd.read_csv('data/students.csv')
courses = pd.read_csv('data/courses.csv')
enrollments = pd.read_csv('data/enrollments.csv')
sessions = pd.read_csv('data/sessions.csv')

# merge data
df = enrollments.merge(students,on= 'Student_ID',how = 'left')
df = df.merge(courses, on = 'Course_ID',how = 'left')

#Fill missing scrors with mean
mean_scores = np.round(np.nanmean(df['Score']),2)
df['Score'] = df['Score'].fillna(mean_scores)

#Create Scores bands
df['Score_Band'] = np.where(df['Score']>=85,'High',
                   np.where(df['Score']>=75,'Medium','Low'))

                   
# Completion Rate Per Cource            
total_enrollments = df.groupby('Course_Name').size()
completed = df[df['Completion_Status'] == 'Completed'].groupby('Course_Name').size()
completion_rate = (completed / total_enrollments * 100).round(2).sort_values(ascending=False)
print("\n Completion Rate per Course:\n", completion_rate)

# Averge Score Per Course
avg_score = df.groupby('Category')['Score'].mean().round(2).sort_values(ascending =False)
print("\n Average Score per Course:\n", avg_score)

# Most Active Student (total time)

active_students = sessions.groupby('Student_ID')['Duration'].sum().sort_values(ascending=False)
most_active = active_students.head(10).reset_index().merge(students,on ='Student_ID',how = 'left')
print("\n Top 10 Active Students:\n", most_active)

# country wise complted status
total_by_country = df.groupby('Country').size()
completed_by_country = df[df['Completion_Status']=='Completed'].groupby('Country').size()
country_success_rate = (completed_by_country / total_by_country * 100).round(2).sort_values(ascending = False)
print("\n Country-wise Course Completion Rate:\n", country_success_rate)

# Step 9: Heatmap Prep (Day vs Month)
# ===============================
sessions['Session_Date'] = pd.to_datetime(sessions['Session_Date'])
sessions['Day'] = sessions['Session_Date'].dt.day_name()
sessions['Month'] = sessions['Session_Date'].dt.month_name()

heatmap_data = sessions.groupby(['Day', 'Month'])['Duration'].sum().reset_index()

# ===============================
# Step 10: Export Cleaned Data (for SQL & Power BI)
# ===============================
df.to_csv("cleaned_enrollments.csv", index=False)
heatmap_data.to_csv("heatmap_sessions.csv", index=False)
most_active.to_csv("active_students.csv", index=False)

print("\n Exported for Power BI and SQL")

