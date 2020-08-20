import tkinter as tk
from tkinter import * 
from actions import * 
import threading

class ExecutorThreadInfo(threading.Thread):
    def __init__(self, player):
        threading.Thread.__init__(self)
        self.player = player
        
    
    def run(self):
        PlayerInfo(self.player).mainloop()
        
class ExecutorThreadDialogue(threading.Thread):
    def __init__(self, player, game):
        threading.Thread.__init__(self)
        self.player = player
        self.game = game
        
    
    def run(self):
        DialogueWindow(self.player, self.game).create()
        
class DialogueWindow(tk.Tk):
    def __init__(self, player, game):
        tk.Tk.__init__(self)

        self.game = game
        self.geometry('400x250')
        self.title("Action")
        self.value = IntVar()
        self.hyp_frame = None
        self.acu_frame = None
    
            
    def create(self):
        frame = Frame(self,)
        frame.grid( row=0, column=0, sticky='WNSE')
        Radiobutton(frame, text='Hypothèse',variable=self.value, value=2, command=self.action_hypothese).grid(row=0, column=1, sticky='W')
        Radiobutton(frame, text='Accusation',variable=self.value, value=3, command=self.action_accusation).grid(row=0, column=2, sticky='W')
        self.mainloop()

    
    def action_hypothese(self,):
        # cree un object hypothese et le renvoyer
        self.hyp_frame = Frame(master=self)
        self.hyp_frame.grid(row=1, column=0, sticky='WNSE')
        Label(self.hyp_frame, text='Suspect').grid(row=0, column=0 , sticky='W')
        self.suspect = Entry(self.hyp_frame)
        self.suspect.grid(row=0, column=1)
        
        Label(self.hyp_frame, text='Arme').grid(row=1, column=0, sticky='W')
        self.arme = Entry(self.hyp_frame)
        self.arme.grid(row=1, column=1)
        
        Label(self.hyp_frame, text='Lieu').grid(row=2, column=0, sticky='W')
        self.lieu = Entry(self.hyp_frame)
        self.lieu.grid(row=2, column=1)
        
        Button(self.hyp_frame, text='verifier', command=self.on_hyp).grid(row=3, column=0, sticky='NS', pady=15, padx=15)
    

    def action_accusation(self):
         
        # cree un object hypothese et le renvoyer
        self.hyp_frame = Frame(master=self)
        self.hyp_frame.grid(row=1, column=0, sticky='WNSE')
        Label(self.hyp_frame, text='Suspect').grid(row=0, column=0 , sticky='W')
        self.suspect = Entry(self.hyp_frame)
        self.suspect.grid(row=0, column=1)
        
        Label(self.hyp_frame, text='Arme').grid(row=1, column=0, sticky='W')
        self.arme = Entry(self.hyp_frame)
        self.arme.grid(row=1, column=1)
        
        Label(self.hyp_frame, text='Lieu').grid(row=2, column=0, sticky='W')
        self.lieu = Entry(self.hyp_frame)
        self.lieu.grid(row=2, column=1)
        
        Button(self.hyp_frame, text='verifier', command=self.on_acuse).grid(row=3, column=0, sticky='NS', pady=15, padx=15)
    
    def on_hyp(self):
        Hypothese(self.suspect, self.arme, self.lieu).match_with_other_players_sheet(self.game.player, self.game.players)
        self.game.current_player_info.destroy()
        self.current_player_info = PlayerInfo(self.game.player)
    def on_acuse(self,):
        if Accusation(self.suspect.get(), self.arme.get(), self.lieu.get()).match_with_solution(self.game.solution):
            messagebox.showinfo('Info', 'Tu a résolue le meurtre')
        else:
            messagebox.showinfo('Info', 'Mauvaise réponse')
            self.game.players.remove(self.game.player)
            self.game.players_sprite.remove(self.game.player)
            self.game.next_player()
    

class PlayerInfo(tk.Tk):
    def __init__(self, player):
        tk.Tk.__init__(self,)
        # loop through the cards
        self.geometry('300x550')
        # frame = Frame(master=self)
        self.title('Info sur le joueur ')
        # Label(master=frame, text='Your Cards').grid(row=1, column=0, sticky="W")
        carte_frame = LabelFrame(self, text='Cartes')
        for row, carte in enumerate(player.cartes):
            Label(carte_frame, text=carte.nom).grid(sticky='W', row=row, column=0)
        # loop through the detective sheet
        # Label(master=frame, text='Your Detective sheet').grid(row=2, column=0, sticky="W")
        carte_frame.grid(row=0, column=0, sticky='NSWE')
        enquete_frame = LabelFrame(self, text='Feuille enquete')
        
        
        suspect_frame = Frame(enquete_frame)
        for row, suspect in enumerate(player.feuille.suspects.items()):
            Label(suspect_frame, text = suspect[0]).grid(row=row, column=0, sticky='W')
            if suspect[1]:
                Label(suspect_frame, text = 'X').grid(row=row, column=1, sticky='W')
            else:
                Label(suspect_frame, text = 'Non deviner').grid(row=row, column=1, sticky='W')


        arme_frame = Frame(enquete_frame)
        for row, suspect in enumerate(player.feuille.armes.items()):
            Label(arme_frame, text = suspect[0]).grid(row=row, column=0, sticky='W')
            if suspect[1]:
                Label(arme_frame, text = 'X').grid(row=row, column=1, sticky='W')
            else:
                Label(arme_frame, text = 'Non deviner').grid(row=row, column=1, sticky='W')


        lieux_frame = Frame(enquete_frame)
        for row, suspect in enumerate(player.feuille.lieux.items()):
            Label(lieux_frame, text = suspect[0]).grid(row=row, column=0, sticky='W')
            if suspect[1]:
                Label(lieux_frame, text = 'X').grid(row=row, column=1, sticky='W')
            else:
                Label(lieux_frame, text = 'Non deviner').grid(row=row, column=1, sticky='W')
        
        suspect_frame.grid(row=0, column=0, sticky='NSWE')
        arme_frame.grid(row=1, column=0, sticky='NSWE')
        lieux_frame.grid(row=2, column=0, sticky='NSWE')
        enquete_frame.grid(row=1, column=0, sticky='NSWE')
        
        
    def create(self):
        self.mainloop()
        
        
class DiceInfo(Tk):
    
    def __init__(self, score):
        Tk.__init__(self)
        Label(self, text=f'Tu peux faire {score} deplacement').grid(row=0, column=0)
        self.mainloop()
        
        
        
        

