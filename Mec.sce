function By = reaction_2(P, d, w, a, b, L)
    P_d = 0;
    for i = 1:length(P)
        P_d = P_d + P(i) * d(i);
    end
    By = -(P_d - w * (b - a) * ((a + b) / 2)) / L;
endfunction

function Ay = reaction_1(P, d, w, a, b, L)
    B = reaction_2(P, d, w, a, b, L);
    Ay = -(-w * (b - a) + sum(P) + B);
endfunction

L = 5;
w = 25000;
a = 3;
b = 5;
p1 = -60000;
d1 = 2;
P = [p1];
d = [d1];

By = reaction_2(P, d, w, a, b, L);
Ay = reaction_1(P, d, w, a, b, L);

x = 0:0.001:L;
V = zeros(size(x));
M = zeros(size(x));

for i = 1:length(x)
    if x(i) >= 0 && x(i) <= d1 then
        V(i) = Ay;
        M(i) = V(i)*x(i);
        continue
    end

    if x(i) > d1 && x(i) <= a then
        V(i) = V(x==d1) + p1;
        M(i) = V(i)*x(i) - V(i)*d1 + M(x==d1); 
        continue
    end

    if x(i) > a && x(i) < b then
        V(i) = -w * x(i) + w*a + V(x == a);
        M(i) = -0.5*w*x(i)^2 + w*a*x(i) + V(x == a)*x(i) -(-0.5*w*a^2 + w*a^2 + V(x==a)*a) + M(x==a);
        continue
    end
    
    if x(i) == L then
        V(i) = 0;
        M(i) = 0;
        continue
    end
end



subplot(2, 1, 1);
plot(x, V, 'b');
xgrid();
xlabel('x');
ylabel('V(x)');
title('Esforço cortante');

subplot(2, 1, 2);
plot(x, M, 'r');
xgrid();
xlabel('x');
ylabel('M(x)');
title('Momento fletor');
