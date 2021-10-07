import projects

if __name__ == "__main__":
    new_project = projects.Project("9/1/20", "9/3/20", "High")
    print(new_project.calc_full_days())