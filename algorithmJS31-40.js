// 프로그래머스 | 부족한 예산 찾기
// https://programmers.co.kr/learn/courses/30/lessons/82612
// 가우스 공식
function solution(price, money, count) {
    const total = price * count * (count + 1) / 2 - money;
    return total > 0 ? total : 0;
}
// console.log(solution(3,20,4))



// 프로그래머스 | 완주하지 못한 선수
// https://programmers.co.kr/learn/courses/30/lessons/42576
function solution1(participant, completion) {
    participant.sort();
    completion.sort();
    for(let i in participant) {
        if(participant[i] !== completion[i]) return participant[i];
    }
}
// console.log(solution1(["leo", "kiki", "eden"], ["eden", "kiki"]))



// 프로그래머스 | 서울에서 김서방 찾기
// https://programmers.co.kr/learn/courses/30/lessons/12919
function solution2(seoul) {
    const kimIndex = seoul.indexOf("Kim");
    return `김서방은 ${kimIndex}에 있다`
}
// console.log(solution2(["Jane", "Kim"]))



// 프로그래머스 | 가장 큰 수
// https://programmers.co.kr/learn/courses/30/lessons/42746
function solution3(numbers) {
    let strNum = numbers.map(num => num + "");
    const answer = strNum.sort((a, b) => (b + a) - (a + b)).join("");
    return answer[0] === "0" ? "0" : answer;
}
// console.log(solution3([6, 10, 2]))



// 프로그래머스 | 예산
// https://programmers.co.kr/learn/courses/30/lessons/12982
function solution4(d, budget) {
    d.sort((a, b) => a - b);
    while (d.reduce((a, b) => (a + b), 0) > budget) {
    d.pop();
    }
    return d.length;
}
// console.log(solution4([2,2,3,3], 10))



// 프로그래머스 | 없는 숫자 더하기
// https://programmers.co.kr/learn/courses/30/lessons/86051
function solution5(numbers) {
    var answer = 45-numbers.reduce((acc,cur) => acc+cur);
    return answer;
}
function solution5(numbers) {
    return 45 - numbers.reduce((acc, cur) => acc + cur, 0);
}
console.log(solution5([1,2,3,4,6,7,8,0]))



// 프로그래머스 | 문자열 내 마음대로 정하기
// https://programmers.co.kr/learn/courses/30/lessons/12915
// sort() => 배열. sort((a, b) =>{});
function solution6(strings, n) {
    strings.sort((a,b)=>{
        if(a[n] > b[n]) return 1;
        if(b[n] > a[n]) return -1;

        if(a > b) return 1;
        if(b > a) return -1;

        return 0;
    });
    return strings;
}
//다른 사람 풀이
function solution6(strings, n) {
    // strings 배열
    // n 번째 문자열 비교
    return strings.sort((s1, s2) => s1[n] === s2[n] ? s1.localeCompare(s2) : s1[n].localeCompare(s2[n]));
}
console.log(solution6(["sun", "bed", "car"], 1))



// 프로그래머스 | 신고 결과 받기
// https://programmers.co.kr/learn/courses/30/lessons/92334
function solution7(id_list, report, k) {
    const newRepo = [...new Set(report)]; // report 중복 제거
    const out = []; // 정지 아이디
    const count = Array(id_list.length).fill(0); // 신고수 [0,0,0,0]
    const mail = Array(id_list.length).fill(0); // 메일수 [0,0,0,0]

    for (let r of newRepo) {
        let a = r.split(" ")[0]; // 유저 ID
        let b = r.split(" ")[1]; // 유저가 신고한 ID
        let idxB = id_list.indexOf(b); // id_list에서 신고받은 유저의 index 칮기
        count[idxB] += 1; // 신고받은 유저의 신고수 누적 더하기

        // 신고수가 k개 이상인 경우
        if (count[idxB] >= k) {
        // 정지 리스트에 해당 아아디 추가
        out.push(id_list[idxB])
        }
    }
    newRepo.map((r, idx) => {
        let a = r.split(' ')[0] // 유저 ID
        let b = r.split(' ')[1] // 유저가 신고한 ID
        // 신고한 ID(b)에 정지된 ID가 있는지 확인
        if (out.indexOf(b) >= 0) {
        // 신고한 ID 중에 정지된 ID가 있다면, 
        // 해당 유저(a)의 id_list에서의 인덱스를 구하고
        // mail의 해당 인덱스에 1 더하기
            let idx = id_list.indexOf(a);
            mail[idx] += 1;
        } 
    }) 
    return mail
}
console.log(solution7(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))




// 프로그래머스 | 하샤드 수 
// https://programmers.co.kr/learn/courses/30/lessons/12947
function solution8(x) {
    let answer = true;
    let arr = String(x).split('');
    let sum = 0

    for(let i = 0; i < arr.length; i++) {
        sum += Number(arr[i]);
    }

    if (!(x % sum === 0)) {
        answer = false;
    }
    return answer;
}
// 다른 사람 풀이
function Harshad(n){
    return !(n % (n + "").split("").reduce((a, b) => +b + +a ));
}
console.log(solution8(10))
