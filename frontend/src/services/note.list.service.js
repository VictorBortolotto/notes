import methods from "./methods";
import routes from "./routes";

const header = new Headers({
  'Content-Type': 'application/json'
})

export const createNewNoteList = async(noteList) => {

  const request = {
      method: methods.methods.post,
      headers: header,
      mode: 'cors',
      cache: 'default',
      body: JSON.stringify(noteList)
  }

  let response = await fetch(routes.defaultRoute + routes.noteListRoutes.noteList + routes.noteListRoutes.newNoteList, request).then(response => response.json());
  return response;

}