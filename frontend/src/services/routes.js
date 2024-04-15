const defaultRoute = 'http://localhost:8080'

const loginRoute = {
  login: '/login'
}

const userRoutes = {
  user: '/user',
  newUser: '/new-user',
  newPassword: '/new-password',
  
}

const noteListRoutes = {
  noteList: '/note-list',
  newNoteList: '/new',
  updateNoteListName: '/update-name',
  deleteNoteList: '/delete'
}

const noteRoutes = {
  note: '/note',
  newNote: '/new',
  updateNoteName: '/update-name',
  updateNoteDescritpion: '/update-description',
  deleteNote: '/delete'
}

export default {
  defaultRoute,
  userRoutes,
  noteListRoutes,
  noteRoutes,
  loginRoute
}