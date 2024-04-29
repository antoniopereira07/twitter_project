from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Post, Relationship, Comment, Like

from .forms import UserRegisterForm, PostForm, ProfileUpdateForm, UserUpdateForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def home(request):
    posts = Post.objects.all()
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
        else:
            form = PostForm()

    context = {'posts': posts, 'form': form}
    return render(request, 'twitter/newsfeed.html', context)


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')  # Após excluir a postagem, redirecione para a página inicial

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}! Faça o login agora.')

            # Cria um novo perfil para o novo usuário
            Profile.objects.create(user=user)
            
            return redirect('login')
        else:
            messages.error(request, 'A Senha deve ter 8 Caracteres incluindo números e letras.')
    else:
        form = UserRegisterForm()

    context = {'form' : form}
    return render(request, 'twitter/register.html', context)



def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')

def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    context = {'user':user, 'posts':posts}
    return render(request, 'twitter/profile.html', context)

@login_required
def editar(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm()

    context = {'user_form' : user_form, 'profile_form' : profile_form}
    return render(request, 'twitter/editar.html', context)

@login_required
def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    return redirect('home')

@login_required
def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.get(from_user=current_user.id, to_user=to_user_id)
    rel.delete()
    return redirect('home')


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('home')  # Redirecione para a página inicial ou outra página desejada
    else:
        form = CommentForm()
    # Renderize o mesmo template que você está usando para exibir os tweets
    posts = Post.objects.all()  # Recupere todos os posts para exibir na página
    context = {'form': form, 'posts': posts}  # Passe o formulário e os posts para o contexto
    return render(request, 'twitter/newsfeed.html', context)


def delete_comment(request, comment_id):
    # Busque o comentário pelo ID
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Verifique se o usuário logado é o autor do comentário
    if request.user == comment.user:
        # Se for, exclua o comentário
        comment.delete()
    
    # Redirecione de volta para a página onde o comentário foi feito
    return redirect('home')


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Verifique se o usuário já curtiu a postagem
    if Like.objects.filter(post=post, user=request.user).exists():
        # Se sim, descurta
        Like.objects.filter(post=post, user=request.user).delete()
    else:
        # Se não, curta
        Like.objects.create(post=post, user=request.user)
    # Atualize a contagem de curtidas da postagem
    post.update_likes_count()  # Chame o método update_likes_count() após adicionar ou remover uma curtida
    return redirect('home')
