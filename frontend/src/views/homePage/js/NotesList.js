import { openToast } from "../../../common/js/toast"
import { createNewNoteList } from "../../../services/note.list.service"
import { getSessionStorage, isEmptyOrNull } from "../../../utils/utils"

export function getTestList() {
  const myList = [
      {name: "TESTE 1"},
      {name: "TESTE 2"},
      {name: "TESTE 3"},
      {name: "TESTE 4"},
      {name: "TESTE 5"},
      {name: "TESTE 6"},
      {name: "TESTE 7"},
      {name: "TESTE 8"},
      {name: "TESTE 9"}
    ]
  
  return myList
}

export async function onClickCreateNewTaskList() {
  let name = document.getElementById('list-name').value

  if(isEmptyOrNull(name)){
    openToast('warn', "Please, fill all the fields before to continue!")
    return
  }
  
  const noteList = {
    idUser: getSessionStorage("idUser"),
    name: name
  }

  let response = await createNewNoteList(noteList)

  console.log(response);
  if(response.statusCode === 200){
    openToast('success', response.description)
  }else{
    openToast('error', response.description)
  }
} 

export async function onClickCancelNewTaskList() {
  let modal = document.getElementById('dialog')
  modal.dismiss()
} 

export default {
  getTestList,
  onClickCreateNewTaskList,
  onClickCancelNewTaskList
}