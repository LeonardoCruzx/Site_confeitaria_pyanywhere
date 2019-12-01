function adicionarTotal(valor){
    if(Number.isNaN(parseInt(localStorage.getItem("total")))){
        localStorage.setItem("total",0);
    }  
    var tot = parseInt(localStorage.getItem("total"));
    tot += valor
    document.getElementById("totalid").value = tot;
    localStorage.setItem("total",tot);
}

function adicionaNaLista(valor,nome){
    let itens = new Array();
    if (localStorage.hasOwnProperty("itens")) {
        itens = JSON.parse(localStorage.getItem("itens"));
    }
    itens.push({nome:nome,valor:valor});

    localStorage.setItem("itens", JSON.stringify(itens))
}

function adicionarCarrinho(valor,nome){
    adicionarTotal(valor);
    adicionaNaLista(valor,nome);
}

function limparCarrinho(){
    let itens = new Array();
    localStorage.setItem("total",0);
    localStorage.setItem("itens",JSON.stringify(itens))
    document.getElementById("totalid").value = localStorage.getItem("total");
    document.getElementById("lista").innerHTML = "";
}

function carregarTotal(){
    if(Number.isNaN(parseInt(localStorage.getItem("total")))){
        localStorage.setItem("total",0);
    }
    document.getElementById("totalid").value = localStorage.getItem("total");

}

function carregarCarrinho(){
    carregarTotal();
    let itens = new Array();
    if (localStorage.hasOwnProperty("itens")) {
        itens = JSON.parse(localStorage.getItem("itens"));
    }
    for(var i = 0; i< itens.length;i++){
        var lista = document.getElementById("lista").innerHTML;
        lista = lista + "<li> item: "+itens[i].nome+", Valor: "+itens[i].valor+"</li>";
        document.getElementById("lista").innerHTML = lista;
    }
}