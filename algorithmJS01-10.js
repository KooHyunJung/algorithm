//  프로그래머스 | 두 정수 사이의 합
//  https://programmers.co.kr/learn/courses/30/lessons/12912
// n ~ m 의 사이의 수 합을 구하는 수학적 정의가 있는데 이름이 생각이 안난다..
// (n+m * (|n-m|+1))/2
function solution(a, b) {
    var answer = ((a+b) * (Math.abs(a-b)+1))/2;
    return answer;
}
// console.log(solution(3,5));


// 프로그래머스 | 자연수 뒤집어 배열
// https://programmers.co.kr/learn/courses/30/lessons/12932
// 변수.toString(); - 숫자를 문자열로 변환
// 배열.reverse(); - 배열 뒤집기
// 배열.map(x=>+x); - 배열의 모든 항목을 숫자로 변환
function solution1(n) {
    let re_num = n.toString();
    re_num = Array.from(re_num).reverse().map(x=>+x);
    return re_num
}
// console.log(solution1(12345));


// 프로그래머스 | 가운데 수 가져오기
// https://programmers.co.kr/learn/courses/30/lessons/12903
// Math.floor(숫자 or 연산) - 소수점 버림, 정수 반환
// 배열.slice(n,m); - n ~ m-1까지 반환
// 배열[0] - 인덱스 요소 반환
function solution2(s) {
    let s_length = s.length;
    let answer = Math.floor(s.length / 2)
    if (s_length %2 === 0) {
        return s.slice(answer-1,answer+1);
    }
    else {
        return s[answer];
    }    
}
// 삼항 연산자 사용
function solution2(s) {
    let s_length = s.length;
    let answer = Math.floor(s.length / 2)  

    return s_length %2 === 0 ? s.slice(answer-1,answer+1) : s[answer];
}
// console.log(solution2("abcd"));


// 프로그래머스 |핸드폰 번호 가리기
// https://programmers.co.kr/learn/courses/30/lessons/12948?language=python
// "문자".repeat(n) - 문자를 n번 반복하는 메소드 ... 이런 거 보면 파이썬이 더 직관적인듯..
function solution3(phone_number) {
    var result = "*".repeat(phone_number.length - 4) + phone_number.slice(-4);
    return result;
}
// console.log(solution3("01033334444"));


// 프로그래머스 | 나머지가 1이 되는 수 찾기
//  https://programmers.co.kr/learn/courses/30/lessons/87389
// 반복문, 조건문 사용 2 ~ n-1 사이에서 나머지가 1이 나오는 숫자 출력
function solution4(n) {
    for (var i = 2; i < n; i++) {
        if (n % i === 1) {
            return i;
        }
    }
}
// console.log(solution4(10));


// 프로그래머스 | 나누어 떨어지는 숫자 배열
// https://programmers.co.kr/learn/courses/30/lessons/12910
// 파이썬에서는 for in 사용, 자스에서는 for문 배열 인덱스로 접근 
// arr.sort((a,b)=>a-b); - 배열 오름차순 정렬
// https://celltong.tistory.com/entry/JavaScript-sort-%EB%A9%94%EC%86%8C%EB%93%9C%EB%A1%9C-%EB%B0%B0%EC%97%B4-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0
function solution5(arr, divisor) {
    let answer = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % divisor == 0) {
            answer.push(arr[i]);
        }
        // if(arr[i] % divisor == 0) answer.push(arr[i]); // 이렇게도 작성 가능
    }
    return answer.length == 0 ? [-1] : answer.sort((a,b)=>a-b);
}
// console.log(solution5([5, 9, 7, 10], 5));


// 프로그래머스 | 같은 숫자는 싫어
// https://programmers.co.kr/learn/courses/30/lessons/12906
// js에도 set이 있다니 ..!
// set만 사용하면 Set(2) { 4, 3 } 이렇게 출력되기에 
// 리스트(배열)형태로 출력하도록 [...]로 감싸준다
function solution66(arr) {
    let re_arr = [...new Set(arr)];
    return re_arr;
} // 하지만 문제를 다시 읽어보니 이게 아니었으므로...
function solution6(arr) {
    let answer = [];
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] !== arr[i+1]) {
            answer.push(arr[i]);
        }
    }
    return answer;
}
// 다른 사람 문제 풀이
function solution6(arr) {
    return arr.filter((val,index) => val != arr[index+1]);
}
// console.log(solution6([1,1,3,3,0,1,1]));
// console.log(solution6([4,4,4,3,3]));


// 프로그래머스 | 평균 구하기
// https://programmers.co.kr/learn/courses/30/lessons/12944
// 수도코드 : 배열.총합 / 배열.길이
// python "sum" === js "arr.reduce()"
// ES6문법 : arr.reduce((a, b) => a + b)
// 나... 파이썬이 더 좋아...
function solution7(arr) {
    var arr_sum = arr.reduce(function(a, b){ return a + b; }, 0);
    return arr_sum / arr.length;
}
// console.log(solution7([1,2,3,4]))


// 프로그래머스 | 내적
// https://programmers.co.kr/learn/courses/30/lessons/70128
// 수도코드 
// 반복문 arr1, arr2 같은 인덱스끼리 곱하기
// 반복문 변수 answer 더하기
function solution8(a, b) {
    var answer = 0;
    for(let i = 0; i < a.length; i++) {
        answer += (a[i] * b[i]);
    }
    return answer;
}
// 다른 사람 풀이
// reduce
// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
// https://velog.io/@s_sangs/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%82%B4%EC%A0%81-JavaScript
function solution8(a, b) {
    return a.reduce((acc, _, i) => acc += a[i] * b[i], 0);
}
// console.log(solution8([1,2,3,4], [-3,-1,0,2]))


// 프로그래머스 | 제일 작은 수 제거하기
// https://programmers.co.kr/learn/courses/30/lessons/12935
// indexOf : https://hianna.tistory.com/379
// splice : https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/splice
function solution9(arr) {
    arr.splice(arr.indexOf(Math.min(...(arr), 1)));
    return arr.length ? arr : [-1];
} 
// console.log(solution9([4,3,2,1]))