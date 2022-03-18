const firebaseApp = firebase.initializeApp({
  apiKey: "AIzaSyCQu71WYwXI9YrMgqFrWwUc6Y61Ip9UOCk",
  authDomain: "django-pro-5e480.firebaseapp.com",
  projectId: "django-pro-5e480",
  storageBucket: "django-pro-5e480.appspot.com",
  messagingSenderId: "711310051920",
  appId: "1:711310051920:web:72611dc96b96abb0749f55",
});

function login() {
  const provider = new firebase.auth.GoogleAuthProvider();
  provider.addScope("https://www.googleapis.com/auth/contacts.readonly");

  firebase
    .auth()
    .signInWithPopup(provider)
    .then(function (result) {
      const { credential, user } = result;
      user.getIdToken().then(function (idtoken) {
        var data = { token_id: idtoken };
        axios.post("/api/google-login/", data).then(function (response) {
          console.log(response);
        });
      });
    })
    .catch(function (error) {
      const { code, message } = error;
      console.log(code, message);
    });
}
