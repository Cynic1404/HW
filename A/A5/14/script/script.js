const render = data => {
    const card = `
    <div class="person">
        id:<div class="id">${data.id}</div>
        name:<div class="name">${data.employee_name}</div>
        salary:<div class="salary">${data.employee_salary}</div>
        age:<div class="age">${data.employee_age}</div>
    </div>`

const $card = $(card);
$card.appendTo($('.info'));
}


$.getJSON(
    'http://dummy.restapiexample.com/api/v1/employees',
function(data){
    render(data.data[0]);
});
