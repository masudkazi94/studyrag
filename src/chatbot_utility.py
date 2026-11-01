import os

working_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(working_dir)

def get_chapter_list(selected_subject):
    if selected_subject in ["Biology", "Physics", "Chemistry"]:
        subject_name=selected_subject.lower()
        chapters_list_dir= f"{parent_dir}/data/class_12/{subject_name}"
        if not os.path.exists(chapters_list_dir):
            return ["No data found for this subject"]
        
        chapters_list=os.listdir(chapters_list_dir)
        chapters_list=[x[:-4] for x in chapters_list]
        #chapters_list.sort(key=lambda x: int(x.split('.')[0]))
        return chapters_list
