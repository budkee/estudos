function classTriangulo(l1, l2, l3) {
    if (l1 == l2 && l1 == l3 && l3 ==l2) {
        console.log('Equilátero')
    }
    else if ((l1 == l2 && (l2 != l3)) || (l2 == l3 && (l1 != l3)) || (l3 == l1) && (l1 != l2)) {
        console.log('Isósceles')
    }
    else if (l1 != l2 != l3) {
        console.log('Escaleno')
    }
}

classTriangulo(3,4,5)