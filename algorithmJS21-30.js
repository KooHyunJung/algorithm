// 프로그래머스 | k번째수
// https://programmers.co.kr/learn/courses/30/lessons/42748
// 수도코드 원본 유지, 이차 배열 commands 반복문 돌리기
function solution(array, commands) {
    var answer = [];
    for(let i = 0; i < commands.length; i++) {
        let arr = array.slice(commands[i][0]-1,commands[i][1]).sort((a,b)=>a-b);
        answer.push(arr[commands[i][2]-1])
    }
    return answer;
}
// 다른 사람 풀이 - 좀 더 직관적인듯
function solution(array, commands) {
    return commands.map(v => {
        return array.slice(v[0] - 1, v[1]).sort((a, b) => a - b).slice(v[2] - 1, v[2])[0];
    });
}
// console.log(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]));



// 프로그래머스 | 문자열을 정수로 바꾸기
// https://programmers.co.kr/learn/courses/30/lessons/12925
// Number() :  인자로 전달된 문자열을 Number 변환. 문자나 undefined 등 인자로 전달하면 NaN(Not A Number) 반환.
// parseInt() : 인자로 전달된 문자열을 Number 변환. 실수도 정수로 변환함.
function solution1(s) {
    return Number(s);
}
// console.log(solution1("1234"))



// 프로그래머스 | 문자열 다루기 기본
// https://programmers.co.kr/learn/courses/30/lessons/12918
// isNaN(value) => 'Not a Number'의 약자 문자열이 숫자인지 아닌지 판별 : 이거는 e를 숫자로 인식한다 : 4,5번 불통..
// s.includes('e') => 3번 음수를 숫자로 인식해서 불통...
function solution2(s) {
    if (s.length === 4 || s.length === 6) {
        return s.includes('e') ? false : true;
    }
    return false;
}
//정규표현식 사용 통과된 풀이
function solution2(s) {
    return /^\d{4}$|^\d{6}$/.test(s)
}
// console.log(solution2("e199"))



// 프로그래머스 | 음양 더하기
// https://programmers.co.kr/learn/courses/30/lessons/76501
function solution3(absolutes, signs) {
    let answer = 0;
    for (let i = 0; i < absolutes.length; i++) {
        signs[i] ? answer += absolutes[i] : answer -= absolutes[i];
    }
    return answer;
}
// console.log(solution3([4,7,12], [true,false,true]))



// 프로그래머스 | 정수 내림차순으로 배치하기
// https://programmers.co.kr/learn/courses/30/lessons/12933
function solution4(n) {
    let answer = Number(n.toString().split("").sort((a,b)=>b-a).join(""));
    return answer;
}
// console.log(solution4(118372))



// 프로그래머스 | 행렬에 덧셈
// https://programmers.co.kr/learn/courses/30/lessons/12950
// 행, 열 길이판별 > 이중반복문 안 배열 > 이중반복문 밖 이차배열 생성 
function solution5(arr1, arr2) {
    let answer = [];
    for (let i= 0; i < arr1.length; i++) {
        let a = [];
        for (let j= 0; j < arr1[0].length; j++) {
            a.push(arr1[i][j] + arr2[i][j]);
        }
        answer.push(a);
    }
    return answer;
}
// 다른 사람 풀이
function solution5(A, B) {
    return A.map((a,i) => a.map((b, j) => b + B[i][j]));
}
// console.log(solution5([[1],[2]], [[3],[4]]))



// 프로그래머스 | 튜플
// https://programmers.co.kr/learn/courses/30/lessons/64065
// "{{" , "}}" 제거 > },{ 기준으로 배열 생성 > 가장 긴 배열 출력 
function solution6(s) {
    let answer = [];
    let newStr = s.slice(2,-2).split("},{").sort((a,b)=>b-a);
    return newStr.slice(-1).toString().split(",").map(Number);
}
console.log(solution6("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
