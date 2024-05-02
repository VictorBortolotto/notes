import { openToast } from "../../../common/js/toast"
import { createNewNoteList, getNoteLists } from "../../../services/note.list.service"
import { getLocalStorage, getSessionStorage, isEmptyOrNull, setLocalStorage } from "../../../utils/utils"

export const getNotesLists = async() => {
  let response = await getNoteLists()
  if (response.statusCode === 200){
    let noteList = JSON.stringify(response.obj)
    setLocalStorage('noteLists', noteList)
    return response.obj;
  }else if (response.statusCode === 404){
    openToast('info', response.description)
    return
  }else{
    openToast('error', response.description)
    return
  }

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

  if(response.statusCode === 200){
    let noteList = JSON.parse(getLocalStorage('noteLists'))
    if(isEmptyOrNull(noteList)){
      noteList = []
      noteList[0] = response.obj
    }else{
      noteList.push(response.obj)
    }
    setLocalStorage('noteLists', JSON.stringify(noteList))
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
  getNotesLists,
  onClickCreateNewTaskList,
  onClickCancelNewTaskList
}