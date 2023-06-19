//1. Дэлгэцнээс өгөгдөл авна
//2. Орж ирсэн мэдээллийг санхүүгийн хэсэгт дамжуулна
//3. Дамжуулсан мэдээллээ дэлгэцэнд харуулна
//4. Өрхийн төсөвт тооцоо хийнэ
//5. Эцсийн үлдэгдэл
// Дэлгэцийн харагдах горим
let uiController=(function(){
  return{
      getInput(){
        return{
          type: document.querySelector(".add__type").value,
          description: document.querySelector(".add__description").value,
          value: document.querySelector(".add__value").value
        };
      },
      addListItem: function(item,type){
        let html;
        if(type==='inc'){
          list='.income__list';
          html='<div class="item clearfix" id="income-%id%"><div class="item__description">$$DESCRIPTION$$</div><div class="right clearfix"><div class="item__value">$$VALUE$$</div><div class="item__delete">            <button class="item__delete--btn"><i class="ion-ios-close-outline"></i></button></div>        </div></div>'
        }
        else{
          list='.expenses__list';
          html='<div class="item clearfix" id="expenses-%id%"><div class="item__description">$$DESCRIPTION$$</div><div class="right clearfix"><div class="item__value">$$VALUE$$</div><div class="item__delete">            <button class="item__delete--btn"><i class="ion-ios-close-outline"></i></button></div>        </div></div>'
        }
        html=html.replace('%id%', item.id);
          html=html.replace('$$DESCRIPTION$$', item.description);
          html=html.replace('$$VALUE$$', item.value);
          document.querySelector(list).insertAdjacentHTML('beforeend', html);
      },
      clearfield: function(){
        let fields=document.querySelectorAll('.add__description,.add__value');
        let feildArr=Array.prototype.slice.call(fields);
        feildArr.forEach(function(el){
          el.value='';
        })
        feildArr[0].focus();
      }
    }
})();
// Санхүүгийн горим
let financeController=(function(){
let Income=function(id,description, value){
  this.id=id,
  this.description=description,
  this.value=value
}
let Expense=function(id,description, value){
  this.id=id,
  this.description=description,
  this.value=value
}
let data={
  items:{
    inc:[],
    exp:[]      
  },
  totals:{
    inc:0,
    exp:0
  }    
}
return{
  addItem: function(type,desc,val){
    let item, id;
    if(data.items[type].length===0) id=1
    else{
      id=data.items[type][data.items[type].length-1].id+1
    }
    if(type ==='inc')
    {
      item= new Income(id,desc,val);
    }
    else{
      item=new Expense(id,desc,val);
    }
    data.items[type].push(item);
    return item;
  },
  seeData:function(){
    return data;
  }
}
})();
// Програмуудыг холбох хэсэг
let appController=(function(uiController, financeController){
  let ctrlAddItem = function() {
  let input=uiController.getInput();
  let item=financeController.addItem(
    input.type,
    input.description,
    input.value);
uiController.addListItem(item, input.type);
uiController.clearfield();
console.log(financeController.seeData());
};
document.querySelector(".add__btn").addEventListener("click", function() {
  ctrlAddItem();
});

document.addEventListener("keypress", function(event) {
  if (event.keyCode === 13 || event.which === 13) {
    ctrlAddItem();
  }
});
})(uiController, financeController);
