test_mark=int(input("Enter the Online Exam Mark ="))
internal_mark=int(input("Enter the Internal Mark="))
upscale_mark=int((test_mark/60)*80)
print("Upscaled Mark for 80 =",int(upscale_mark))
total_mark=int
total_mark=upscale_mark+internal_mark
print("Total Mark =",total_mark)
if total_mark>=91:
    grade="O"
elif total_mark>80 and total_mark<=90:
    grade="A+"
elif total_mark>70 and total_mark<=80:
    grade="A"
elif total_mark>60 and total_mark<=70:
    grade="B+"
elif total_mark>50 and total_mark<=60:
    grade="B"
else:
    grade="U"
print("Grade =",grade)