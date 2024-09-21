// formLogin = document.querySelector('#form_login');
// formRegister = document.querySelector('#form_cadastro');
// body = document.querySelector('body');
//
// password = document.querySelector('#password');
// nome = document.querySelector('#username');
//
// nome.addEventListener('blur', (e) => {
//     if (!nome.value)
//         console.log("nome Vazio");
//     else{
//         console.log(nome);
//     }
// });
//
// formLogin.addEventListener('submit', async (e) => {
//     e.preventDefault();
//     const url = 'http://localhost:5000/login/';
//
//     console.log(nome.value);
//     console.log(password.value);
//
//     const data = {
//         name: nome.value,
//         password: password.value,
//     }
//     const res = await fetch(url,
//         {
//             method: 'POST',
//             body: JSON.stringify(data),
//             }).then(res => res.text());
//     console.log(res);
//     document.write(res);
// });
//
// // form.addEventListener('submit', async (e) => {
// //     e.preventDefault();
// //     const url = 'http://localhost:5000/login/';
// //     console.log(nome.value);
// //     console.log(password.value);
// //     const data = {
// //         name: name.value,
// //         password: password.value,
// //     }
// //     const res = await axios.post(url,
// //         {
// //             data,
// //             headers: {
// //                 "Access-Control-Allow-Origin": "*",
// //                 "Access-Control-Allow-Headers": "Authorization",
// //                 "Access-Control-Allow-Methods": "GET, POST, OPTIONS, PUT, PATCH, DELETE" ,
// //                 "Content-Type": "application/json;charset=UTF-8"
// //             }
// //         });
// //     document.write(res.data);
// // });
//
//
