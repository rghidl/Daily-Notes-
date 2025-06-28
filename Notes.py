def show_menu():
   print("\n Daily Notes Menu 📓:"
        "\n 1-Add new note "
        "\n 2-read your notes"
        "\n 3-Exit📍"
        "\n 4-Delete all notes 🗑️"
)

while True:
  show_menu()
  choice=input("\n Choose 1-4:")

  if choice=="1":
    note=input("\n Enter your note:")
    with open("notes.txt","a",encoding="utf-8") as file:
      file.write(note+"\n" )
      print("\n Notes Are Saved✅")

  elif choice=="2":
    try:
      with open("notes.txt","r",encoding="utf-8") as f:
        content=f.read()
        if content.strip()=="":
          print("\n 📭 No notes yet!")
        else:
            print("\n Your Notes:"+"\n"+content)
    except FileNotFoundError:
      print("\n ⚠️ You don’t have notes yet!")    

  elif choice=="3":
    print("\n Goodbye 🖐️")
    break

  elif choice == "4":
        confirm = input("Are you sure you want to delete all notes? (yes/no): ")
        if confirm.lower() == "yes":
            open("notes.txt", "w", encoding="utf-8").close()
            print("\n 🗑️ All notes deleted!")
        else:
            print("\n ❎ Deletion cancelled.")
  else:
    print("\n ❌ Choose only 1,2,3 or 4.")

